import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('../env_vars/100doc_python_env_vars.env')

SENDER_SMTP = 'smtp.gmail.com'
SENDER_EMAIL = os.environ['MY_TEST_GMAIL']
SENDER_PW = os.environ['TEST_GMAIL_APP_PW']  # app password
TO_EMAIL = os.environ['MY_TEST_GMAIL']

product_webpage = 'https://www.amazon.com/dp/B07GF1J5TK/?coliid=I1MY75PU3PFB82&' \
                  'colid=3EPBHINHP8J8L&psc=1&ref_=lv_ov_lig_dp_it'
price_threshold = 300

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

response = requests.get(url=product_webpage, headers=headers)
result = response.text

soup = BeautifulSoup(result, 'lxml')
item_price_tag = soup.find(name='span', class_='a-offscreen')
item_price = float(item_price_tag.get_text().replace('$', ''))
item_name_tag = soup.find(name='span', id='productTitle')
item_name = item_name_tag.get_text().strip()

if item_price <= price_threshold:
    with smtplib.SMTP(SENDER_SMTP) as connection_gmail:
        connection_gmail.starttls()  # creates a secure connection
        connection_gmail.login(user=SENDER_EMAIL, password=SENDER_PW)
        connection_gmail.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:KimKimKim Amazon Price Alert!\n\nKimKimKim Price Alert!\n"
                f"{item_name} is currently ${item_price}. Buy now!\n\n"
                f"Link: {product_webpage}"
        )

