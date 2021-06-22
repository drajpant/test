from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime


# PATH where driver is saved
PATH = "C:\Program Files (x86)\chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://foobar.protonchain.com/")



connect_wallet = driver.find_element(By.XPATH, '//button[text()="Connect Wallet"]')
connect_wallet.click()
print(connect_wallet)
time.sleep(5)

# CLick connect wallet
pro = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/ul/li[1]/span")
pro.click()

# Wait for 15 sec - Time to scan the code and accept the popup in proton app
time.sleep(15) 

number = 1

# For the first time, Get tokens will be clicked

token = driver.find_element(By.XPATH, '//button[text()="Get tokens"]')
token.click()
sleep_time=3610
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Inside Loop: Try " , number, " time = " , current_time )
    print("Sleeping for: ", sleep_time , "s")
    
    time.sleep(sleep_time)
    number = number+1
    # After inital click on Get tokens, Success button will be clicked every hour
    token_success = driver.find_element(By.XPATH, '//button[text()="Success!"]')
    token_success.click()
