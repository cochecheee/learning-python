"""
1. Find a product on Amazon that you want to track and get the product URL or just use the one I'm tracking.

https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6

In addition to the URL, when your browser tries to load up a page in Amazon, it also passes a bunch of other information. e.g. Which browser you're using, which computer you have etc.

These additional pieces of information are passed along in the request Headers.

You can see your browser headers by going to this website:

http://myhttpheader.com/

2. Use the requests library to request the HTML page of the Amazon product using the URL you got from 1.

HINT 1: You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.

HINT 2: Remember this is how you pass headers with the requests library:

https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method

HINT 3: Print the output of the get request and make sure the actual HTML of the web page is printed, if not try adding more items from your header from hint1. Sometimes, Amazon might just return the Captcha page.

3. Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml" parser instead of the "html.parser" for this to work.

HINT: If you get an error that says "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser." Then it means you're not using the right parser, you'll need to import lxml at the top and install the module then use "lxml" instead of "html.parser" when you make soup.

4. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.

HINT: You might need to use the split() method: https://www.w3schools.com/python/ref_string_split.asp
"""
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

URL = "https://www.amazon.com/New-SteelSeries-Apex-Wireless-2023/dp/B0BF67DM6K/ref=sr_1_1_sspa?crid=IVW629A6XRDB&dib=eyJ2IjoiMSJ9.ZZXwxMMr-U0OnFtQq5WXN-KJhlBWoBCJPP3TLgFvKbAzxZvL1KuE_LzUMQPcQhrc3AU4rZx02MfvGgzTrfswk1UU2q-VXbcRPTnjTxAo2igXrzzpVO6fKxcyTiT2Z5wXhbgI5aVAI01-nrK3HYto2lnKZsIyPQu213-sQLUhtHgrIb9MkLjbObtR9B4JSQQ7TJlaZouiqdP7VFKkKXu-WXH-_6hkb_r-TrDPnVSKBFc.PSuhcmZAeYyoZtdvlmQRw2-3XVDzlDIOlGMpoG05llM&dib_tag=se&keywords=mechanical%2Bkeyboard%2Brazer&qid=1720518105&sprefix=mechanical%2Bkeyboard%2Braze%2Caps%2C364&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9,vi;q=0.8"
}

response = requests.get(URL,headers=headers)

contents = response.text

# # take the document
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-price-whole").get_text().strip('.')
cent = soup.find(class_="a-price-fraction").get_text()
currency = "$"

price_tag = float(price) + float(int(cent)/100)
# price_tag = 40


# send mail to the user
if price_tag < 50.00:
    # send mail
    user = "testsmtplib.123@outlook.com"
    passwd = "Hellomaycung@312@@123#*"

    from_addr = "testsmtplib.123@outlook.com"
    to_addr = "buitien747@gmail.com"
    smtp_srv = "smtp.live.com"

    # create the email
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "SteelSeries Apex Pro TKL Wireless HyperMagnetic Gaming Keyboard — Esports Tenkeyless — OLED Screen — Adjustable Actuation — PBT Keycaps — Bluetooth — 2.4GHz — USB-C"

    # body of the email
    body = f"The current price is {price_tag}{currency}, would you like to buy it?"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the server and send the email
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
        connection.starttls() 
        connection.login(user=user, password=passwd)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())



