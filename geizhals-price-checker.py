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

if platform.system() == 'Windows':
    from win10toast import ToastNotifier  # noqa

from geizhals_price_checker.messenger import Messenger
from geizhals_price_checker.product import Product


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
    c = {}
    with open(path, 'r') as f:
        for line in f:
            key, value = re.split(', ', line)
            if key == 'smtp_port':
                c[key] = int(value.rstrip('\n'))
            else:
                c[key] = value.rstrip('\n')

    return c


def check_for_product(products, messenger, recipient):
    error = False

    while error is False:  # Executes the code as long as no heavy errors occur
        for product in products:
            try:
                # -----Getting Website Stuff
                website = Product.get_web_site(product.url)

                price = website.xpath("//*[@id=\"product0\"]/div[6]/span/span")[0].text.strip()
                name = website.xpath("//*[@id=\"product0\"]/div[2]/a/span")[0].text.strip()
                link = "https://geizhals.at/" + website.xpath("//*[@id=\"product0\"]/div[2]/a/@href")[0]
                picture = website.xpath("//*[@id=\"product0\"]/div[1]/a/div/picture/source/@srcset")[0]  # noqa

                price = price.lstrip('€ ')  # removes the euro sign and the space
                price = price.replace(',', '.')  # removes the comma with a dot
                price = float(price)  # converts price string to float
                # -----Getting Website Stuff

                if product.target_price >= price:  # If a product with a good price exists, then send me E-mail
                    # print(f"PREISALARM: {name} ist gerade für {price}€ zu haben!")
                    messenger.send_mail(recipient, name, price, link)  # Calls function to send email WORKS
                    # print("Mail sent ;)")
                    time.sleep(3)

            except urllib.error.URLError:
                # When Internet is down or site returns a 404 this exception is triggered and stops the script
                error = True
                if platform.system() == 'Windows':
                    toaster = ToastNotifier()
                    toaster.show_toast("Geizhals-price-checker error",
                                       f"Netzwerkfehler: Konnte keine Informationen aus "
                                       f"dem Internet Laden, oder Seite returns 404 "
                                       f"Status! Script beendet.", duration=10,
                                       threaded=True)
                else:
                    print(f"Netzwerkfehler: Konnte keine Informationen aus "
                          f"dem Internet Laden, oder Seite returns 404 "
                          f"Status! Script beendet.")
                break
            except IndexError:
                # When a wrong link is being read or a category has 0 products, this exception will be triggered
                if platform.system() == 'Windows':
                    toaster = ToastNotifier()
                    toaster.show_toast("Geizhals-price-checker error",
                                       f"Seiten Ladefehler: Konnte keine Informationen "
                                       f"für Link {product.url} aus dem Internet Laden! "
                                       f"Überprüfe die Links!", duration=240,
                                       threaded=True)
                else:
                    print(f"Seiten Ladefehler: Konnte keine Informationen "
                          f"für Link {product.url} aus dem Internet Laden! "
                          f"Überprüfe die Links!")
        if not error:
            print("Sleep for one hour")
            time.sleep(3600)  # stops the script and waits one hour before polling again


def main():
    import argparse

    # Parser to read email configuration from command line. run python geizhals-price-checker.py --help to get help.
    parser = argparse.ArgumentParser()
    parser.add_argument('--read_config_from_file', type=int, default=1, choices=[0, 1])
    parser.add_argument('--sender', type=str, help='E-Mail address of sender.')
    parser.add_argument('--recipient', type=str, help='E-Mail address of recipient.')
    parser.add_argument('--smtp_pass', type=str, help='Password of sender E-Mail.')
    parser.add_argument('--smtp_host', default='mail.gmx.net', type=str, help='Sender E-Mail host (default: '
                                                                              'mail.gmx.net).')
    parser.add_argument('--smtp_port', default=587, type=int, help='SMTP port to use (default: 587).')
    args = parser.parse_args()

    if (args.sender is None or args.recipient is None or args.smtp_pass is None) and args.read_config_from_file == 0:
        raise ValueError('Please provide `sender`, `recipient`, and `smtp_pass` if `read_config_from_file=0`.')

    data = read_products_from_file('price_list.txt')
    target_prices = data['target_prices']
    urls = data['urls']

    products = []
    for target_price, url in zip(target_prices, urls):
        products.append(Product(target_price, url))

    if args.read_config_from_file:
        config = read_config_from_file('configuration.txt')
    else:
        config = {'sender': args.sender, 'recipient': args.recipient,
                  'smtp_pass': args.smtp_pass, 'smtp_host': args.smtp_host, 'smtp_port': args.smtp_port}

    messenger = Messenger(config)

    check_for_product(products, messenger, recipient=config['recipient'])


if __name__ == '__main__':
    main()
