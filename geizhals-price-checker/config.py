"""Config class"""

import re


class Config(object):
    """Class Config which represents a configuration"""

    def __init__(self):
        pass

    def read(self, path):
        pattern = re.compile(r'^(?:[1-9]\d*|0)?(?:\.\d+)?, https?://[^\s<>"]+|www\.[^\s<>"]+$')

        with open(path, 'r') as f:
            for line in f:
                if pattern.match(line):
                    print(line)

    def write(self):
        pass


def main():
    config = Config()
    config.read('../configuration.txt')


if __name__ == '__main__':
    main()
