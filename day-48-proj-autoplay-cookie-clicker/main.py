from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "http://orteil.dashnet.org/experiments/cookie/"
five_minutes = time.time() + 60*5

driver.get(url)
cookie = driver.find_element(By.ID, "cookie")


def get_store_items():
    store_items = driver.find_elements(By.CSS_SELECTOR, "#store > div")
    item_ids = []
    item_prices = []
    for i in range(len(store_items)-1):
        if store_items[i].get_attribute("class") != "grayed":
            item_ids.append(store_items[i].get_attribute("id"))
            item_prices.append(int(store_items[i].find_element(By.CSS_SELECTOR, "b").text.split(" - ")[1].replace(",", "")))
    if len(item_ids) > 0:
        highest_price_item = item_ids[item_prices.index(max(item_prices))]
        return highest_price_item
    else:
        return ''


while time.time() < five_minutes:
    five_seconds = time.time() + 5
    while time.time() < five_seconds:
        driver.find_element(By.ID, "cookie").click()
    buy_item_id = get_store_items()
    if buy_item_id != '':
        driver.find_element(By.ID, buy_item_id).click()

cookies_per_second = int(driver.find_element(By.ID, "cps").text.split(" : ")[1])
print(cookies_per_second)

driver.close()

