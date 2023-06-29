from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\\Users\\admin\\Downloads\\chromedriver_win32 (1)\\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.prohance.net/?adgroup=&network=s&device=c&placement=&utm_campaign=&utm_source=adwords&utm_medium=ppc&utm_term=productivity%20software&hsa_acc=4596767980&hsa_cam=11700347910&hsa_grp=126378477338&hsa_ad=535045277707&hsa_src=s&hsa_tgt=kwd-11870936&hsa_kw=productivity%20software&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=EAIaIQobChMIv7CP-uip9wIVTZNmAh1KkQh4EAAYASAAEgJxQPD_BwE")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Modules").click()
sm=driver.find_element(By.LINK_TEXT,"Work Time")
sm.click()
print("is displayed",sm.is_displayed())
time.sleep(3)
wm=driver.find_element(By.LINK_TEXT,"Workflow Module")
print("IS DISPLAYed",wm.is_displayed())
wm.click()








  #clicksonnlogin






