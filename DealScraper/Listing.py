from PyQt6.QtCore import QObject, pyqtSignal
import requests


class Listing(QObject):

    def __init__(self, title, url, buy_price):
        super().__init__()
        self.title = title  # user_setting
        self.url = url  # user_setting
        self.buy_price = buy_price  # user-setting

        self.image_url = ""  # get from url => name="productImageUrl"
        self.scraped_title = ""  # get from url => name="productTitle"
        self.currency = ""  # get from url => "name=\"priceSymbol\""
        self.og_price = ""  # get from url => scraped price at time of entry
        self.current_price = ""  # get from url => scraped price as of this run

        self.custom_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'accept-language': 'en-US,en;q=0.5',
        }

        self.scrape('f')

    def scrape(self, *d):
        response = requests.get(self.url, headers=self.custom_headers)

        arr = response.text.split(' ')
        for i in range(len(arr)):
            if arr[i] == "name=\"priceSymbol\"":
                self.currency = arr[i + 1].split("\"")[1]
                print(self.currency) # WRITE TO FILE
            elif arr[i] == "name=\"priceValue\"":
                p_string = arr[i + 1]
                self.current_price = float(p_string.split("\"")[1])
                if d == 'f':
                    self.og_price = self.current_price
                print(self.current_price) # WRITE TO FILE
