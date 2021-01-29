#!/usr/bin/env python3
from urllib.request import Request, urlopen




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

print(webpage.decode('utf8'))


