# setup and run the handler and SysTrayIcon
from SysTrayIcon import MainWindow
try:
    import winxpgui as win32gui
except ImportError:
    import win32gui


def main():
    w = MainWindow()
    win32gui.PumpMessages()


if __name__ == "__main__":
    main()

# Minimal self test. You'll need a bunch of ICO files in the current working
# directory in order for this to work...

'''
if __name__ == '__main__':
    import itertools, glob

    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "SysTrayIcon.py Demo"
    def hello(sysTrayIcon): print("Hello World.")
    def simon(sysTrayIcon): print("Hello Simon.")
    def switch_icon(sysTrayIcon):
        sysTrayIcon.icon = icons.next()
        sysTrayIcon.refresh_icon()
    menu_options = (('Say Hello', icons.next(), hello),
                    ('Switch Icon', None, switch_icon),
                    ('A sub-menu', icons.next(), (('Say Hello to Simon', icons.next(), simon),
                                                  ('Switch Icon', icons.next(), switch_icon),
                                                  ))
                    )
    def bye(sysTrayIcon): print('Bye, then.')

    SysTrayIcon(icons.next(), hover_text, menu_options, on_quit=bye, default_menu_index=1)
    
'''

'''
prototype code

import requests

default_currency = "INR"

watch_urls = [] # populate using data file, remember to read in at the start and write at new entry (/end of session?)
buy_currencies = [] # default if not changed - get 3-letter currency codes
buy_prices = [] # if less than or equal to this price, display webpage

url2 = "https://www.amazon.in/HP-Pavilion-Micro-Edge-Graphics-13-be2055AU/dp/B0BXLP2H4W/ref=sr_1_4?crid=1IVF1ZLS15SYZ&dib=eyJ2IjoiMSJ9.yULTw61F4fy5jAeM_jbHzovCur_7gYwLKyewTwHDBTbirJiYAzWUNFyqtD4I-MheSY4wWmHk3HllMnUvNFRoTc1WhjuSBNBoPOWs_lczaqfQRn3N_80ZzZ64HjSlC73fYAqqzw3pB0CaeSVEwTEMjVlxyCzt0C2OpVKJUMXJahO2c6Y_o945GJh1Kp7AGV8BzuuV4eXW_Sp0_5pQ-kRESM3VuDisuK-BEO-fPiTg3Ks.Zffm1XXP1-fFZGbdcvYF6-NGgLliZqkrn-KePHtQPHs&dib_tag=se&keywords=hp+pavilion+aero+13&qid=1714461584&sprefix=%2Caps%2C472&sr=8-4"
url = "https://www.amazon.in/Dell-Inspiron-5430-i7-1360P-Processor/dp/B0C91QWF1X/ref=sr_1_2?crid=1KHF24B738TF2&dib=eyJ2IjoiMSJ9.R1DffFJ4i2VenjwZGiM32YdsPd8zt0JtHr4fCqi2_S95y6P0lFfNSAxhFPs1CaLLLuW_7XvC7MY4QN6BBHQ_sds1r5glwLXIlz-2YRi976utI6S_n1FPULnKCXkvqmSXzfPkfcKPULAYW5RuecH3yczsYsXH8jHxR9wWkFsU7D0cYADaNgsKzVLiS7AvgGG99FNrQ5gyC-WwFBo6bSzhugulCFxQ-HcXjtst8JvSnTh_R5SdmvqlV5tdbwV9BhnqJV3YHjxo6qSzsRbhon6-8T76nnkSJyKjtyiwIakxizA.iHfnP7bW-Ag7cb945S5wWKkFebNNRreFKswyIHCTtjk&dib_tag=se&keywords=dell+inspiron&qid=1714462482&refinements=p_n_feature_twenty-six_browse-bin%3A27399069031&rnid=27399067031&s=computers&sprefix=dell+inspiron%2Caps%2C237&sr=1-2"

custom_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'accept-language': 'en-US,en;q=0.5',
}

response = requests.get(url, headers=custom_headers)

arr = response.text.split(' ')
price = float("inf")
currency = ""
for i in range(len(arr)):
    if arr[i] == "name=\"priceSymbol\"":
        currency = arr[i+1].split("\"")[1]
        print(currency)
    elif arr[i] == "name=\"priceValue\"":
        p_string = arr[i+1]
        price = float(p_string.split("\"")[1])
        print(price)
        break

#print(response.text)
'''
