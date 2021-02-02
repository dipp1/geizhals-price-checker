"""Class messenger"""

import platform
from email.message import EmailMessage
from smtplib import SMTP
from win10toast import ToastNotifier


class Messenger(object):
    """Class Messenger that sends messages"""

    def __init__(self, config):
        self.sender = config['sender']
        self.smtp_user = config['smtp_user']
        self.smtp_pass = config['smtp_pass']
        self.smtp_host = config['smtp_host']
        self.smtp_port = config['smtp_port']

    def send_mail(self, recipient, product_name, product_price, product_url):
        msg = EmailMessage()
        message_string = f"PREISALARM: {product_name} ist gerade für {product_price}€ zu haben!\n"
        message_string = message_string + f"Näheres zum Produkt findest du hier: {product_url}"
        msg.set_content(message_string)
        msg['Subject'] = f"PREISALARM vom Geizhalschecker, {product_name} für {product_price}€ zu haben!"
        msg['From'] = self.sender
        msg['To'] = recipient

        try:
            with SMTP(host=self.smtp_host, port=self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.smtp_user, self.smtp_pass)
                smtp.send_message(msg)
                print("Email gesendet")
        except Exception as e:
            print("Problem beim E-Mail versenden")
            print(e)
            if platform.system() == 'Windows':
                toaster = ToastNotifier()
                toaster.show_toast("Geizhals-price-checker error",
                                   f"{product_name} wurde für {product_price}€ gefunden, "
                                   f"aber durch Internetprobleme konnte die Mail nicht "
                                   f"gesendet werden. :(", duration=50, threaded=True)
