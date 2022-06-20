import requests
import datetime as dt
import os
from twilio.rest import Client

STOCK = "EA"
COMPANY_NAME = "Electronic Arts Inc"

AV_URL = "https://www.alphavantage.co/query"
AV_API_KEY = os.environ['ALPHAVANTAGE_API_KY']

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ['NEWSAPI_API_KEY']

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['MY_TWILIO_PHONE']
MY_NUMBER = os.environ['MY_VERIFIED_PHONE']

pct_threshold = 5

def is_weekday():
    if dt.datetime.now().weekday in range(4):
        return True
    else:
        return False

def format_pct_change(pct_change):
    if pct_change > 0:
        return f"🔺{round(pct_change, 1)}%"
    elif pct_change < 0:
        return f"🔻{round(pct_change, 1)}%"
    else:
        return f"No change"

def format_emoji(pct_change):
    if pct_change > 0:
        return " 📈 "
    elif pct_change < 0:
        return " 📉 "

def format_article(art):
    article = \
        f"""{STOCK}: {format_pct_change(pct_diff)}\n
        Headline: {art[0]}\n
        Brief: {art[1]}"""
    return article

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

r = requests.get(AV_URL, params=av_params)
data = r.json()["Time Series (Daily)"]
last_day = float(list(data.items())[:2][0][1]["4. close"])
prior_day = float(list(data.items())[:2][1][1]["4. close"])
pct_diff = (last_day - prior_day) / prior_day * 100

if pct_diff >= pct_threshold or pct_diff <= -pct_threshold:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "pageSize": 3,
        "page": 1
    }

    r = requests.get(NEWS_URL, params=news_params)
    r.raise_for_status()
    data = r.json()["articles"]
    news_list = [(item["title"], item["description"]) for item in data]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

notify = client.messages \
                .create(
                     body=f'Stock Alert for EA!{format_emoji(pct_diff)}',
                     from_=TWILIO_NUMBER,
                     to=MY_NUMBER
                 )

for article in news_list:
    send_article = client.messages \
                    .create(
                         body=format_article(article),
                         from_=TWILIO_NUMBER,
                         to=MY_NUMBER
                     )

# #Optional: Format the SMS message like this:
# f"""
# {STOCK}: {format_pct_change(pct_diff)}
# Headline: {news_list[0][0]}
# Brief: {news_list[0][1]}
# {STOCK}: {format_pct_change(pct_diff)}
# Headline: {news_list[1][0]}
# Brief: {news_list[1][1]}
# {STOCK}: {format}
# Headline: {news_list[2][0]}
# Brief: {news_list[2][1]}
# """

