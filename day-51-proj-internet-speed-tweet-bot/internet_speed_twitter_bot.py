from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import requests
from requests_oauthlib import OAuth1Session
import os
from dotenv import load_dotenv
import json

load_dotenv('../env_vars/100doc_python_env_vars.env')

CHROME_DRIVER_PATH = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'

TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(45)
        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        self.driver.close()

    def tweet_at_provider(self):
        payload = {"text": f"TEST: Hey [internet provider] why are my speeds low? Down: {self.down}Mbps / {self.up}Mbps"}
        # Get request token
        # Make the request
        oauth = OAuth1Session(
            TWITTER_API_KEY,
            client_secret=TWITTER_API_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_SECRET,
        )

        # Making the request
        response = oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )

        print("Response code: {}".format(response.status_code))

        # Saving the response as JSON
        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))
        print()