#!/usr/bin/env python3

"""
Authors: Tiberiu-Arthur Nowotny, Buraczewska Diana
Purpose of this script: Reads geizhals links and checks for required prices periodically
Last updaten on:
"""

import platform
import re
import time
import urllib.error

from geizhals_price_checker.messenger import Messenger
from geizhals_price_checker.product import Product

if platform.system() == 'Windows':
    from win10toast import ToastNotifier


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


def read_config_from_file(path):
    # sender, smtp_user, smtp_pass, smtp_host, smtp_port
    c = {}
    with open(path, 'r') as f:
        for line in f:
            key, value = re.split(', ', line)
            if key == 'smtp_port':
                c[key] = int(value)
            else:
                c[key] = value

    return c


def check_for_product(products, messenger, recipient=None):
    if recipient is None:
        recipient = messenger.sender

    error = False

    while error is False:  # Executes the code as long as no heavy errors occur
        for product in products:
            try:
                # -----Getting Website Stuff
                website = Product.get_web_site(product.url)

                price = website.xpath("//*[@id=\"product0\"]/div[6]/span/span")[0].text.strip()
                name = website.xpath("//*[@id=\"product0\"]/div[2]/a/span")[0].text.strip()
                link = "https://geizhals.at/" + website.xpath("//*[@id=\"product0\"]/div[2]/a/@href")[0]
                picture = website.xpath("//*[@id=\"product0\"]/div[1]/a/div/picture/source/@srcset")[0]

                price = price.lstrip('€ ')  # removes the euro sign and the space
                price = price.replace(',', '.')  # removes the comma with a dot
                price = float(price)  # converts price string to float
                # -----Getting Website Stuff

                if product.target_price >= price:  # If a product with a good price exists, then send me E-mail
                    print(f"PREISALARM: {name} ist gerade für {price}€ zu haben!")
                    messenger.send_mail(recipient, name, price, link)  # Calls function to send email WORKS
                    time.sleep(3)

            except urllib.error.URLError:
                error = True
                if platform.system() == 'Windows':
                    toaster = ToastNotifier()
                    toaster.show_toast("Geizhals-price-checker error", f"Netzwerkfehler: Konnte keine Informationen "
                                                                       f"aus dem Internet Laden! Script beendet.",
                                       duration=10, threaded=True)
                break
            except IndexError:
                if platform.system() == 'Windows':
                    toaster = ToastNotifier()
                    toaster.show_toast("Geizhals-price-checker error", f"Seiten Ladefehler: Konnte keine "
                                                                       f"Informationen für Link {product.url} aus "
                                                                       f"dem Internet Laden! Überprüfe die Links!",
                                       duration=240, threaded=True)

        print("Sleep for one hour")
        time.sleep(3600)  # stops the script and waits one hour before polling again


def main():
    data = read_products_from_file('price_list.txt')
    target_prices = data['target_prices']
    urls = data['urls']

    products = []
    for target_price, url in zip(target_prices, urls):
        print(target_price, url)
        products.append(Product(target_price, url))

    config = read_config_from_file('configuration.txt')

    messenger = Messenger(config)

    check_for_product(products, messenger)


if __name__ == '__main__':
    main()
