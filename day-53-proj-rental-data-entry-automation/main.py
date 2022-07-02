# # Steps:
# ----------------- #
# TODO 0: Import Selenium and BeautifulSoup, dotenv+os (if necessary), and time (sleep)
# TODO 1: Make a function to scrape listings from Zillow city search
# TODO 2: Create lists of links, prices, and addresses
# TODO 3: Fill in the form for each listing

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from time import sleep


GOOGLE_FORM_LINK = 'https://forms.gle/2FfmcvpUbhbFF8kX6'
ZILLOW_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22' \
              'pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22' \
              'west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22' \
              'south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22' \
              'isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3A' \
              'true%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22' \
              'value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22' \
              'value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22' \
              'fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3A' \
              'false%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22' \
              'max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22' \
              'beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22' \
              'mapZoom%22%3A12%7D'

HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
CHROME_DRIVER_PATH = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
links = []
prices = []
addresses = []

response = requests.get(url=ZILLOW_LINK, headers=HEADERS)
z_page = response.text
soup = BeautifulSoup(z_page, 'html.parser')
for link in soup.select('.list-card-top a'):
    href = link['href']
    if link is not None:
        if 'http' not in href:
            links.append(f"https://www.zillow.com{href}")
        else:
            links.append(href)
addresses = [listing.getText().split(" | ")[-1] for listing in soup.find_all(class_='list-card-addr')]
prices = [listing.getText() for listing in soup.find_all(class_='list-card-price')]

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
for i in range(len(addresses)):
    driver.get(GOOGLE_FORM_LINK)
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addresses[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

