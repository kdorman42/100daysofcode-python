##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib as mail
import random as r
import datetime as dt
import pandas as pd
import os

PLACEHOLDER = '[NAME]'
SENDER_SMTP = "smtp.mail.yahoo.com"
MY_EMAIL = os.environ['MY_TEST_YMAIL']
MY_PASSWORD = os.environ['TEST_YMAIL_APP_PW']  # app password

bday_data = pd.read_csv('birthdays.csv')

now = dt.datetime.now()
today_birthdays = {row["name"]: row.email for (index, row) in bday_data.iterrows()
                   if row.month == now.month and row.day == now.day}

if len(today_birthdays) > 0:
    letter_choice = r.randint(1, 3)
    with open(f"./letter_templates/letter_3.txt") as letter_file:
        letter_template = letter_file.read()
    for (key, value) in today_birthdays.items():
        new_letter = letter_template.replace(PLACEHOLDER, key.split()[0])
        subject=f"Subject:Happy Birthday, {key.split()[0]}!"
        to_email = value
        with mail.SMTP(SENDER_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=f"{subject}\n\n{new_letter}"
            )




