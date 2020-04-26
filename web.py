import os, sys, time 
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

handle   = os.getenv("handle")
password = os.getenv("password")

f = open("contestID.txt",'r')
id = f.read()
f.close()

driver = webdriver.Chrome(executable_path='/home/seek/driver/chromedriver') #path where you downloaded chromedriver
driver.get(f"https://codeforces.com/contestRegistration/{id}/virtual/true")

ele = driver.find_element_by_id("handleOrEmail")
ele.send_keys(handle)
ele = driver.find_element_by_id("password")
ele.send_keys(password)
ele.send_keys(Keys.RETURN)

time.sleep(10)

driver.find_element_by_css_selector('.submit').click()
