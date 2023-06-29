from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("C:\\Users\\admin\\Downloads\\chromedriver_win32 (1)\\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news/heropanti-2-review-runway-34-movie-review-box-office-collection-update-live-updates-tiger-shroff-ajay-devgn-tara-sutaria-bollywood/liveblog/91166794.cms")
driver.maximize_window()
driver.switch_to_alert().dismiss()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/nav/ul/li[6]/a").click()






