#!/usr/bin/env python3
from urllib.request import Request, urlopen
from html5_parser import parse
from lxml.etree import tostring




'''
Authors: Tiberiu-Arthur Nowotny, Buraczewska Diana
Purpose of this script: Reads geizhals links and checks for required prices periodically
Last updaten on:
'''

'''TODO DIANA
Create file configuration
Read file and create a list / array of links
Implement save config method

config example

[Geizhals Links]
geizhals.at/....
geizhals.at/....
geizhals.at/....
etc.
'''



'''TODO Arthur

Create method to iterate over list /array
Get html site and search for matching price in geizhals table

'''
link = 'https://geizhals.at/?cat=monlcd19wide&xf=11939_23~11955_IPS~11963_144~14591_19201080&asuch=&bpmin=&bpmax=&v=e&hloc=at&plz=&dist=&mail=&sort=p&bl1_id=30#productlist'


# from urllib import request
#
# with request.urlopen(link, headers={'User-Agent': 'Mozilla/5.0'}) as response:
#     data = response.read()
#
def get_webSite():
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    return  urlopen(req).read()





webpage = get_webSite() # Contains all HTML from the site
root = parse(webpage)

price = root.xpath("//*[@id=\"product0\"]/div[6]/span/span")[0].text.strip()
name = root.xpath("//*[@id=\"product0\"]/div[2]/a/span")[0].text.strip()
link = "https://geizhals.at/" + root.xpath("//*[@id=\"product0\"]/div[2]/a/@href")[0]
picture = root.xpath("//*[@id=\"product0\"]/div[1]/a/div/picture/img/@big-image-url")[0]
# the @ refers to the attribute of the selected element, / slashes seem to separate the searched terms
# The [0] refers to the first element of a list, we use this because xPath returns a list with exactly one item

price = price.lstrip('€ ') # removes the euro sign and the space
price = price.replace(',', '.') # removes the comma with a dot
price = float(price) # converts price string to float
price = price + 30

print(f"Price : {price}")
print("Name : " + (name))
print("Link : " + (link))
print("PictureLink : " + (picture))

if (price <= 200.2):
    print('PRICE LOW BUYYYYYYYYYYYYYYYYY')

res = isinstance(price, str)

# print result
print("Is variable a string ? : " + str(res))



# print(webpage.decode('utf8'))


