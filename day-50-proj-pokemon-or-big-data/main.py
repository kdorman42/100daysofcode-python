from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import unidecode

chrome_driver_path = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

quiz_url = 'https://pixelastic.github.io/pokemonorbigdata/'


def google_answer(qname):
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.google.com')
    sleep(1)
    driver.find_element(By.NAME, "q").send_keys(qname)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    sleep(2)
    first_result_raw = driver.find_element(By.CSS_SELECTOR, "#search h3")
    first_result = unidecode.unidecode(first_result_raw.text.lower())
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return first_result


def choose_answer(g_result):
    if "pokemon" in g_result:
        driver.find_element(By.CLASS_NAME, "question-button-pokemon").click()
    else:
        driver.find_element(By.CLASS_NAME, "question-button-bigdata").click()


driver.get(quiz_url)
sleep(1)
score = -1
while score < 0:
    try:
        driver.find_element(By.CLASS_NAME, "endscreen")
    except NoSuchElementException:
        question_name = driver.find_element(By.CLASS_NAME, "question-name").text
        result = google_answer(question_name)
        choose_answer(result)
        sleep(1)
        driver.find_element(By.CLASS_NAME, "answer-button-next").click()
    else:
        score = int(driver.find_element(By.CSS_SELECTOR, "span[data-reactid='.0.0.1']").text)
        print(f"You got {score}% correct!")

driver.close()










