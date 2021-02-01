#!/usr/bin/env python3
"""
Authors:                    Tiberiu-Arthur Nowotny, Buraczewska Diana
Purpose of this script:     Reads Geizhals links and checks for required prices periodically
Last updated on:            01.02.2021
"""

from urllib.request import Request, urlopen
from lxml import html

# TODO DIANA
"""
Create file configuration
Read file and create a list / array of links
Implement save config method

config example

[Geizhals Links]
15.99, geizhals.at/....
312.50,geizhals.at/....
250, geizhals.at/....
etc.
"""

# TODO Arthur
"""
Create method to iterate over list /array
Get html site and search for matching price in geizhals table
"""

# link = 'https://geizhals.at/?cat=monlcd19wide&xf=11939_23~11955_IPS~11963_144~14591_19201080&asuch=&bpmin=&bpmax=&v
# =e' \ '&hloc=at&plz=&dist=&mail=&sort=p&bl1_id=30#productlist ' link =
# 'https://geizhals.at/?cat=monlcd19wide&v=e&hloc=at&sort=p&bl1_id=30&xf=11939_23%7E11955_IPS%7E11963_240
# %7E14591_19201080' link = 'https://geizhals.at/?cat=cpuamdam4&xf=25_6%7E5_PCIe+4.0%7E5_SMT%7E820_AM4'
link = "https://geizhals.eu/?cat=sysdiv&xf=3126_1920x1080~8419_sonstige&asuch=&bpmin=&bpmax=&v=e&hloc=at&hloc=de&hloc" \
       "=pl&hloc=uk&hloc=eu&plz=&dist=&mail=&sort=p&bl1_id=30#productlist "


def get_webSite():
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    return urlopen(req).read()

webpage = get_webSite()  # Contains all HTML from the site
root = html.fromstring(webpage)

price = root.xpath("//*[@id=\"product0\"]/div[6]/span/span")[0].text.strip()
name = root.xpath("//*[@id=\"product0\"]/div[2]/a/span")[0].text.strip()
link = "https://geizhals.at/" + root.xpath("//*[@id=\"product0\"]/div[2]/a/@href")[0]
# picture = root.xpath("//*[@id=\"product0\"]/div[1]/a/div/picture/img/@big-image-url")[0]
picture = root.xpath("//*[@id=\"product0\"]/div[1]/a/div/picture/source/@srcset")[0]
# picture = picture.lstrip('https://gzhls.at/i/61/20/2436120-s0.jpg x1, ')
# the @ refers to the attribute of the selected element, / slashes seem to separate the searched terms
# The [0] refers to the first element of a list, we use this because xPath returns a list with exactly one item

price = price.lstrip('€ ')  # removes the euro sign and the space
price = price.replace(',', '.')  # removes the comma with a dot
price = float(price)  # converts price string to float
price = price + 30

print(f"Price : {price}")
print("Name : " + name)
print("Link : " + link)
print("PictureLink : " + (picture.split(" ")[2]))

a_list = ["Kater", "Mauser", "Hunder"]

for animal in a_list:
    print(animal)








product = Product(200, "www.google.at")
product.changeName()
print(product.askPrice)

if (price <= 200.2):
    print('PRICE LOW BUYYYYYYYYYYYYYYYYY')


#Check the type of some variable
res = isinstance(price, str)

# print result
print("Is variable a string ? : " + str(res))



# print(webpage.decode('utf8'))


