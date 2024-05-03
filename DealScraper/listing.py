from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QWidget
import requests


class Listing(QWidget):

    def __init__(self, title, url, buy_price):
        super().__init__()
        self.title_box = QLineEdit(title)  # user_setting
        self.url_text = url
        self.url_box = QLineEdit(url)  # user_setting
        self.buy_price_box = QLineEdit(str(buy_price))  # user-setting

        self.image_url = ""  # get from url => name="productImageUrl"
        self.scraped_title = ""  # get from url => name="productTitle"
        self.currency = ""  # get from url => "name=\"priceSymbol\""
        self.current_price = ""  # get from url => scraped price as of this run

        self.custom_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'accept-language': 'en-US,en;q=0.5',
        }

        self.scrape('f')

        self.current_price_box = QLineEdit(str(self.current_price))

        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.title_box)
        self.hbox.addWidget(self.buy_price_box)
        self.hbox.addWidget(self.current_price_box)
        self.hbox.addWidget(self.url_box)

        self.setLayout(self.hbox)

    def scrape(self, *d):
        response = requests.get(self.url_text, headers=self.custom_headers)

        arr = response.text.split(' ')
        for i in range(len(arr)):
            if arr[i] == "name=\"priceSymbol\"":
                self.currency = arr[i + 1].split("\"")[1]
            elif arr[i] == "name=\"priceValue\"":
                p_string = arr[i + 1]
                self.current_price = float(p_string.split("\"")[1])
