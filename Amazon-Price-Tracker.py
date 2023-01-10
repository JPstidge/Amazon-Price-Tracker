# AMAZON PRICE TRACKER

import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "THE URL OF YOUR PRODUCT"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="sns-base-price").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


#SEND AN EMAIL ALERT

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200000000
EMAIL = "YOUR EMAIL @ .com"
PASSWORD = "YOUR PASSWORD"

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: SUBJECT!\n\n{message}\nHere is the link to buy!\n{url}"
        )