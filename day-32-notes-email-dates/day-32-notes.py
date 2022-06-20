import smtplib
import os

sender_smtp = "smtp.gmail.com"
my_email = os.environ['MY_TEST_GMAIL']
my_password = os.environ['TEST_GMAIL_APP_PW']  # gmail app password
to_email = os.environ['MY_TEST_YMAIL']

sender_smtp = "smtp.mail.yahoo.com"
my_email = os.environ['MY_TEST_YMAIL']
my_password = os.environ['TEST_YMAIL_APP_PW']  # ymail app password
to_email = os.environ['MY_TEST_GMAIL']

# Similar to opening and closing files, this can be replaced with 'with + as'.
connection_gmail = smtplib.SMTP("smtp.gmail.com")
connection_gmail.close()

# Gmail requires an "app password" set up in security settings to send from py.

with smtplib.SMTP(sender_smtp) as connection_gmail:
    connection_gmail.starttls()  # creates a secure connection
    connection_gmail.login(user=my_email, password=my_password)
    connection_gmail.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject:Hello\n\nThis is ths body of my email"
    )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(year))
print(type(now))
print(day_of_week)  # 0 is monday

if year == 2020:
    print("Wear a face mask.")

date_of_birth = dt.datetime(year=1983, month=12, day=1, hour=16)  # only ymd are required
print(date_of_birth)

