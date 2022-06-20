import smtplib
import datetime as dt
import random

# ---- CONSTANTS ---- #
sender_smtp = "smtp.gmail.com"
my_email = os.environ['MY_TEST_GMAIL']
my_password = os.environ['TEST_GMAIL_APP_PW']  # app password
to_email = os.environ['MY_TEST_YMAIL']
weekday_name = "Tuesday"
weekday_id = 1


# ---- SEND MAIL FUNCTION ---- #
def send_weekly_quote():

    with open('quotes.txt') as data_file:
        data = data_file.readlines()

    quote_text = random.choice(data)

    with smtplib.SMTP(sender_smtp) as connection_gmail:
        connection_gmail.starttls()  # creates a secure connection
        connection_gmail.login(user=my_email, password=my_password)
        connection_gmail.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{weekday_name} Motivation\n\n{quote_text}"
        )


# ---- SEND IF WEEKDAY MATCH ---- #
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == weekday_id:
    send_weekly_quote()
