#!/usr/bin/env python3
'''
Authors: Tiberiu-Arthur Nowotny, Buraczewska Diana
Purpose of this script: Reads geizhals links and checks for required prices periodically
Last updaten on:
'''
import re
from urllib.request import Request, urlopen
from lxml import html
import urllib.error
from smtplib import SMTP
from email.message import EmailMessage
from win10toast import ToastNotifier
import time
import webbrowser
# toaster = ToastNotifier()
# toaster.show_toast("Sample Notification","Python is awesome!!!", duration=50, threaded=True)
'''TODO DIANA
Create file configuration
Read file and create a list / array of links
Implement save config method

config example

[Geizhals Links]
15.99, geizhals.at/....
312.50,geizhals.at/....
250, geizhals.at/....
etc.
'''



'''TODO Arthur

Create method to iterate over list /array
Get html site and search for matching price in geizhals table

'''

'''



Zuerst File eingelesen

Zuerst überprüfen ob link gültig
Objekt erstellen -> wenn irgendwo index 0 -> objekt nicht erstellen


'''



class Product:  # Class Product which needs a price and link, represents a product

    def __init__(self, askPrice, link):
        self.link = link
        self.askPrice = askPrice


def get_webSite(link):  # returns a HTML page which can be read by the xPath
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    return html.fromstring(urlopen(req).read())


def read_products_from_file(path):
    pattern = re.compile(r'^(?:[1-9]\d*|0)?(?:\.\d+)?, https?://[^\s<>"]+|www\.[^\s<>"]+$')

    d = {'target_prices': [], 'urls': []}
    with open(path, 'r') as f:
        for line in f:
            if pattern.match(line):
                price, url = re.split(', ', line)
                d['target_prices'].append(float(price))
                d['urls'].append(url)

    return d


def main():
    data = read_products_from_file('price_list.txt')
    target_prices = data['target_prices']
    urls = data['urls']

    products = []
    for target_price, url in zip(target_prices, urls):
        products.append(Product(target_price, url))

    checkForProduct(products)


def checkForProduct(aList):
    aList = aList
    i = 0
    error = False

    while (error == False): # Executes the code as long as no heavy errors occur
        # print("----Neuer Durchlauf!---")
        while i < len(aList): # Iterates over every Productlist Object
            # print(f"Produkt {i + 1} wird analysiert")
            try:
                #-----Getting Website Stuff
                website = get_webSite(aList[i].link)
                produktListObject = aList[i]

                price = website.xpath("//*[@id=\"product0\"]/div[6]/span/span")[0].text.strip()
                name = website.xpath("//*[@id=\"product0\"]/div[2]/a/span")[0].text.strip()
                link = "https://geizhals.at/" + website.xpath("//*[@id=\"product0\"]/div[2]/a/@href")[0]
                picture = website.xpath("//*[@id=\"product0\"]/div[1]/a/div/picture/source/@srcset")[0]
                # the @ refers to the attribute of the selected element, / slashes seem to separate the searched terms
                # The [0] refers to the first element of a list, we use this because xPath returns a list with exactly one item

                price = price.lstrip('€ ') # removes the euro sign and the space
                price = price.replace(',', '.') # removes the comma with a dot
                price = float(price) # converts price string to float
                #-----Getting Website Stuff



                if (produktListObject.askPrice >= price): # If a product with a good price exists, then send me E-mail
                    print(f"PREISALARM: {name} ist gerade für {price}€ zu haben!")
                    sendMail(name, price, link) # Calls function to send email WORKS
                    time.sleep(3)




            except urllib.error.URLError as e:
                error = True
                toaster = ToastNotifier()
                toaster.show_toast("Geizhals-price-checker error", f"Netzwerkfehler: Konnte keine Informationen aus dem Internet Laden! Script beendet." , duration=10, threaded=True)
                # print(f"Error status is: {error}")
                break
            except IndexError:
                # print("Could not get any information of the product list. Wrong link or no products.")
                toaster = ToastNotifier()
                toaster.show_toast("Geizhals-price-checker error", f"Seiten Ladefehler: Konnte keine Informationen für Link Nummer {i + 1} aus dem Internet Laden! Überprüfe die Links!" , duration=240, threaded=True)


            i += 1 # auti increment of our counter variable for our for loop
        i = 0 # Sets our i for the "for loop" to 0 after being done with the loop, so that it can restart when the while loop restarts

        # print("Sleep for one hour")
        # time.sleep(3600) # stops the script and waits one hour before polling again
        time.sleep(8)



    # if (error == False):
    #     print("We do something")
    # else:
    #     print("We had an error and do nothing")


def sendMail(productName, productPrice, productLink):
    sender = 'python-testscript@gmx.at'
    recipient = 'max.nowotny.512@gmail.com'
    smtp_user = sender
    smtp_pass = "MeinPasswort1!"
    smtp_host = "mail.gmx.net"
    smtp_port = "587"

    msg = EmailMessage()
    message_string = f"PREISALARM: {productName} ist gerade für {productPrice}€ zu haben!\n"
    message_string = message_string + f"Näheres zum Produkt findest du hier: {productLink}"
    msg.set_content(message_string)
    msg['Subject'] = f"PREISALARM vom Geizhalschecker, {productName} für {productPrice}€ zu haben!"
    msg['From'] = sender
    msg['To'] = recipient
    try:
        with SMTP (host=smtp_host, port=smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_user,smtp_pass)
            smtp.send_message(msg)
            print("Email sent")
    except Exception as e:
        print("Problem beim E-Mail versenden")
        print(e)
        toaster = ToastNotifier()
        toaster.show_toast("Geizhals-price-checker error", f"{productName} wurde für {productPrice}€ gefunden, aber duch Internetprobleme konnte die Mail nicht gesendet werden. :(" , duration=50, threaded=True)
main()