## About
### Authors/Contributors
Tiberiu-Arthur Nowotny<br>
Diana Buraczewska<br>

### Description
This script will take a link of a specific Geizhals product cathegory and will check if there is a product matching your asking price.

### Main focus of this project
This project focus on:
- [x] Access to Files
- [x] Regex
- [x] Windows 10 Desktop Notifications
- [x] Email Notifications
- [x] External Data Sources (Web Scraping from Geizhals.at)


## Installation/Prerequisites for your repository
To use this script you need to install the following libraries:
* lxml
* win10toast

You install them by opening up cmd in administrator mode and then typing
```
pip install [the library you want]
```
example:
```
pip install lxml
```

## Run/Execute
To run the program you'll need to follow the following steps: <br>
1. Go to [Geizhals.at](https://geizhals.at)<br>
2. Select a Product category <br>
3. Select the properties of the products you're looking for <br>
4. Click on "Sortieren nach" (sort by) "Bestpreis" (best price) <br>
5. Now copy the link from your browser and open the Preisliste.txt file <br>
6. Insert the price you're looking for and the link of the product category. <br>
If the desired price contains a decimal point, use a dot instead. <br>Separate price and link with a decimal.<br>
for example:
```
210.36, https://geizhals.at/?cat=cpuamdam4&xf=25_6%7E2_7nm%7E4_65%7E6679_12%7E820_AM4
```
7. Now it's time to configure the  <br>

[Nothing here (yet)]


## Documentation
[Nothing here (yet)]

## Known Issues
[Nothing here (yet)]


## Useful links
[Pandao markdown editor ](https://pandao.github.io/editor.md/en.html)<br>
[Stackedit markdown editor ](https://stackedit.io/app#)
