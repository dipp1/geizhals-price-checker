"""Product class"""

from urllib.request import Request, urlopen


class Product(object):
    """Class Product which needs a price and link, represents a product"""
    price = 0.0
    name = ""
    link = ""
    pictureLink = ""

    def __init__(self, ask_price, link):
        self.link = link
        self.ask_price = ask_price

    def get_web_site(self):
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        return urlopen(req).read()

    def change_name(self):
        self.name = "Lepin :D"