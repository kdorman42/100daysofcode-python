from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.followers = []

    def login(self, username, pw):
        login_url = 'https://www.instagram.com/accounts/login/'
        self.driver.get(login_url)
        sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(pw)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        sleep(3)

        # handle "save login info" by clicking "not now"
        try:
            self.driver.find_element(By.CLASS_NAME, "olLwo")
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(By.CSS_SELECTOR, ".cmbtv button").click()
            sleep(3)

        try:
            self.driver.find_element(By.CLASS_NAME, "_a9_1").text
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(By.CLASS_NAME, "_a9_1").click()
            sleep(3)

    def find_followers(self, acct):
        acct_url = f'https://www.instagram.com/{acct}/'
        self.driver.get(acct_url)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, f"a[href='/{acct}/followers/']").click()
        sleep(5)
        self.followers = self.driver.find_elements(By.CSS_SELECTOR, "div[role='dialog'] button")
        print(len(self.followers))

    def follow(self):
        old_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            sleep(2)
            if new_height == old_height:
                break
            old_height = new_height

        # for account in self.followers:
        #     if account.find_element(By.CSS_SELECTOR, "button div").text in ["Follow"]:
        #         account.find_element(By.CSS_SELECTOR, "button div").click()
        #         sleep(1)

