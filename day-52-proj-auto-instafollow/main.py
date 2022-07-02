from instafollower import InstaFollower
from dotenv import load_dotenv
import os

load_dotenv('../env_vars/100doc_python_env_vars.env')

CHROME_DRIVER_PATH = 'C:/Users/kdorman/PycharmProjects/drivers/chromedriver.exe'
INSTA_USER = os.environ['INSTA_USER']
INSTA_PW = os.environ['INSTA_PW']
SIMILAR_ACCOUNT = 'kimprobable42'

bot = InstaFollower(driver_path=CHROME_DRIVER_PATH)
bot.login(username=INSTA_USER, pw=INSTA_PW)
bot.find_followers(acct=SIMILAR_ACCOUNT)
bot.follow()



