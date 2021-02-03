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

Alternatively, if you use conda, simply run
```
conda env create -f environment.yml
```
This will create the conda environment geizhals-price-checker
including all dependencies.


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
You can add as many links as you want to this file. Just make sure that they comply with this format.<br>
<b>NOTE: The list contains a few examples already. You can safely replace them. </b>

7. Now it's time to configure the E-Mail functionality: 
   * Open up the configuration.txt in Notepad or similiar text editor
   * Now you'll see this: 
```
sender, sender.email@mail.com
recipient, recipient.email@mail.com
smtp_pass, SenderPassword
smtp_host, smtp-host.of-sender.net
smtp_port, 587
```
Now just replace the placeholders with the right credentials of your E-Mail addresses, smtp host and port and you're good to go!<br>

Example: <br>
"I want to send E-Mails from my gmx address to my Google-Mail E-Mail address as soon as I one product matches my desired price"
```
sender, my-gmx-address@gmx.at
recipient, my-google-mail.address@mail.com
smtp_pass, MySecretPasswort_123456#12!
smtp_host, mail.gmx.net
smtp_port, 587
```
<b>NOTE: You may need to add a different SMTP server and Port depending on which E-Mail provider you use for your Sender E-Mail!
This kind of information can be found on DuckDuckGo or just contact your internet provider for more information!</b>

## Known Issues
* The library "win10toast" is currently missing out on updates and will make this script crash if invalid configuration data is provided.
* Sometimes the "win10toast" library will crash the script if multiple windows notifications get generated
* The library "win10toast" is windows only. The script runs without the library. However, note that you have to remove that dependency from environment.yml if you do not use Windows.

## Useful links
[Pandao markdown editor ](https://pandao.github.io/editor.md/en.html)<br>
[Stackedit markdown editor ](https://stackedit.io/app#)<br>
[Geizhals.at](https://geizhals.at)