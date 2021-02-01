"""Config class"""

from urllib.request import Request, urlopen

from lxml import html


class Product(object):
    """Class Product which needs a price and link, represents a product"""

    def __init__(self, target_price, url):
        self.target_price = target_price
        self.url = url

    @staticmethod
    def get_web_site(link, user_agent='Mozilla/5.0'):
        """Returns a HTML page which can be read by the xPath"""
        req = Request(link, headers={'User-Agent': user_agent})
        return html.fromstring(urlopen(req).read())

    @staticmethod
    def write_to_file(target_price, url, path):
        with open(path, 'w+') as f:
            f.write('{0}, {1}'.format(target_price, url))


def main():
    product = Product(100.0, 'test')
    print(product.target_price, product.url)
    product.write_to_file(10.0, 'test', '../price_list-write.txt')


if __name__ == '__main__':
    main()
