from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome_driver_path = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
# driver = webdriver.Chrome(chrome_driver_path)
#
# driver.get("https://www.amazon.com/dp/B07GF1J5TK/?coliid=I1MY75PU3PFB82&colid=3EPBHINHP8J8L&psc=1&ref_=lv_ov_lig_dp_it")
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_text = price.text
# print(price_text)
# # note that finding an element by name is useful for forms / search forms
#
# driver.close()  # closes a single tab (the active one)
# # driver.quit()  # shuts down the entire browser

chrome_driver_path = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "https://www.python.org/"

driver.get(url)
event_times = [item.text for item in driver.find_elements(By.CSS_SELECTOR, value=".event-widget > .shrubbery > .menu > li > time")]
event_names = [item.text for item in driver.find_elements(By.CSS_SELECTOR, value=".event-widget > .shrubbery > .menu > li > a")]

driver.close()

event_dict = {i: {event_times[i]: event_names[i]} for i in range(len(event_times))}
print(event_dict)