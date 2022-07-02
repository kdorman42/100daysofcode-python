from dotenv import load_dotenv
import os
from internet_speed_twitter_bot import *

load_dotenv('../env_vars/100doc_python_env_vars.env')

PROMISED_DOWN = 500
PROMISED_UP = 100


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()



