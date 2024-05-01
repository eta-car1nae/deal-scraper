import Listing
import schedule
import time

listings = [] # populate listings


def scrape_listings(s):
    if s == 'all':
        for listing in listings:
            listing.scrape()


schedule.every().day.at("00:00").do(scrape_listings, 'all')
schedule.every().day.at("06:00").do(scrape_listings, 'all')
schedule.every().day.at("12:00").do(scrape_listings, 'all')
schedule.every().day.at("18:00").do(scrape_listings, 'all')

#current test
schedule.every().day.at("14:50").do(scrape_listings, 'all')

while True:
    schedule.run_pending()
    time.sleep(3600)
