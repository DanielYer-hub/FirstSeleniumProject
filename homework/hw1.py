# В FirstSeleniumProject создайте новый тестовый класс
# и в нем тестовый метод, который найдет по тэгу 10 элементов
# на https://demowebshop.tricentis.com/ с использованием стратегии
# By.NAME , By.CLASS_NAME , By.ID  и By.CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
   driver.get("https://demowebshop.tricentis.com/")

   ul = driver.find_element(By.TAG_NAME,"ul")
   ul1 = driver.find_element(By.CSS_SELECTOR,"ul")

   form = driver.find_element(By.TAG_NAME,"form")
   form1 = driver.find_element(By.CSS_SELECTOR,"form")

   h3 = driver.find_element(By.TAG_NAME,"h3")
   h3_1 = driver.find_element(By.CSS_SELECTOR,"h3")

   close = driver.find_element(By.CLASS_NAME,"close")
   close1 = driver.find_element(By.CSS_SELECTOR,"close")

   footer = driver.find_element(By.CLASS_NAME,"footer")
   footer1 = driver.find_element(By.CSS_SELECTOR,"footer")

   header = driver.find_element(By.CLASS_NAME,"header")
   header1 = driver.find_element(By.CSS_SELECTOR,"header")

   account = driver.find_element(By.CLASS_NAME,"account")
   account1 = driver.find_element(By.CSS_SELECTOR,"account")

   bar_notification = driver.find_element(By.ID,"bar-notification")
   bar_notification1 = driver.find_element(By.CSS_SELECTOR,"#bar-notification")

   dialog = driver.find_element(By.ID,"dialog-notifications-success")
   dialog1 = driver.find_element(By.CSS_SELECTOR,"#dialog-notifications-success")


finally:
    driver.quit()