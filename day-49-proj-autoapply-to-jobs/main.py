from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv('../env_vars/100doc_python_env_vars.env')

LINKEDIN_TEST_USERNAME = os.environ['LINKEDIN_TEST_USERNAME']
LINKEDIN_TEST_PW = os.environ['LINKEDIN_TEST_PW']

chrome_driver_path = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "https://www.linkedin.com/jobs/search/?currentJobId=3135675479&distance=25.0&f_AL=true&geoId=101165590&keywords=social%20media%20manager"
driver.get(url)

driver.find_element(By.LINK_TEXT, value='Sign in').click()
sleep(3)

driver.find_element(By.ID, value="username").send_keys(LINKEDIN_TEST_USERNAME)
driver.find_element(By.ID, value="password").send_keys(LINKEDIN_TEST_PW)
driver.find_element(By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
sleep(2)

jobs_list = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
for job in jobs_list:
    job.click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, value="jobs-apply-button").click()
    sleep(2)
    try:
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application' i]")
    except NoSuchElementException:
        pass
    else:
        driver.find_element(By.CSS_SELECTOR, "input[data-test-single-line-text-input]").send_keys("9999999999")
        driver.find_element(By.CSS_SELECTOR, "label[for='follow-company-checkbox']").click()
    finally:
        driver.find_element(By.CSS_SELECTOR, value='button[data-test-modal-close-btn]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, value='button[data-test-dialog-secondary-btn]').click()



# driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div[2]/div/div/input").send_keys("9999999999")
# driver.find_element(By.CSS_SELECTOR, value="button[data-easy-apply-next-button]").click()
# sleep(2)
# driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
# sleep(2)
# driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[1]/label').click()
# sleep(2)
# # driver.find_element(By.ID, value="ember138").click()  # Applies for the job
#
# driver.find_element(By.CSS_SELECTOR, value='button[data-test-modal-close-btn]').click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR, value='button[data-test-dialog-primary-btn]').click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR, value='button[data-test-modal-close-btn]').click()
# sleep(1)





