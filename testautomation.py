from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\\Users\\admin\\Downloads\\chromedriver_win32 (1)\\chromedriver")
driver=webdriver.Chrome(service=serv_obj)   #declaringdriverandaccessitfromdevicelocation
driver.get("https://demo.nopcommerce.com")    #link of the website
print(driver.title)   #title of the page
driver.get("http://newtours.demoaut.com/")

print(driver.title)           #navigation through different websites
time.sleep(5)                   #waitingfor load
driver.back() 
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)


