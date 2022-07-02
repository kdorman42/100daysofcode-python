from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

# url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(url)
#
# # article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # article_count.click()
#
# # driver.find_element(By.LINK_TEXT, value="Content portals").click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("wombat")
# # driver.find_element(By.CSS_SELECTOR, value="#searchButton").click()  # clicks the search icon
# search.send_keys(Keys.ENTER)  # hits enter to search

# driver.close()

# Example: fill out newsletter signup on appbrewery
url = 'http://secure-retreat-92358.herokuapp.com/'
driver.get(url)

driver.find_element(By.NAME, value="fName").send_keys("Kay")
driver.find_element(By.NAME, value="lName").send_keys("Dormant")
driver.find_element(By.NAME, value="email").send_keys("kdormant.dev.test@gmail.com")
driver.find_element(By.CLASS_NAME, value="btn").click()

driver.close()
