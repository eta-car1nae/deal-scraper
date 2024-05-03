from listing import Listing
import schedule
import time

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
import pandas as pd


class Handler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listings Handler")
        self.csv_file = 'listings.csv'

        self.listings = []  # populate from file

        self.populate_from_csv()

        button = QPushButton("Tester!")
        button.clicked.connect(self.button_clicked)

        self.details_title = QLabel("Title")
        self.details_og_price = QLabel("OG Price")
        self.details_buy_price = QLabel("Buy Price")
        self.details_url = QLabel("URL")

        self.details_title.setAlignment(Qt.AlignHCenter)
        self.details_og_price.setAlignment(Qt.AlignHCenter)
        self.details_buy_price.setAlignment(Qt.AlignHCenter)
        self.details_url.setAlignment(Qt.AlignHCenter)

        self.wid = QWidget()
        self.vbox = QVBoxLayout(self.wid)

        self.labels_widget = QWidget()
        self.labels = QHBoxLayout(self.labels_widget)
        self.labels.addWidget(self.details_title)
        self.labels.addWidget(self.details_og_price)
        self.labels.addWidget(self.details_buy_price)
        self.labels.addWidget(self.details_url)

        self.vbox.addWidget(self.labels_widget)

        for list_item in self.listings:
            self.vbox.addWidget(list_item)

        self.wid.setLayout(self.vbox)
        self.setCentralWidget(self.wid)

    def scrape_listings(self, s):
        if s == 'all':
            for list_item in self.listings:
                list_item.scrape()

    def button_clicked(self):
        print("Button Clicked")

    def populate_from_csv(self):
        csv_listings = pd.read_csv(self.csv_file)
        for f in range(len(csv_listings.index)):
            entries = csv_listings.iloc[f]
            self.listings.append(Listing(entries[0], entries[1], entries[2]))

    '''schedule.every().day.at("00:00").do(scrape_listings, 'all')
    schedule.every().day.at("06:00").do(scrape_listings, 'all')
    schedule.every().day.at("12:00").do(scrape_listings, 'all')
    schedule.every().day.at("18:00").do(scrape_listings, 'all')

    # current test
    schedule.every().day.at("14:50").do(scrape_listings, 'all')

    while True:
        schedule.run_pending()
        time.sleep(3600)'''