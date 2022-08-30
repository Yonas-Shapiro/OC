# Main file for selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from languages import switchLanguage

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#driver.close()
vmNum = input("VM num: ")
site = "http://192.168.2." + str(vmNum) + "/otcs/cs.exe?func=llworkspace"

driver.get(site)
print(driver.title)

driver.find_element(By.ID, "otds_username").send_keys("Admin")
driver.find_element(By.ID, "otds_password").send_keys("livelink")
driver.find_element(By.ID, "otds_password").send_keys(Keys.RETURN)

print(driver.title)



switchLanguage(driver, "de", site)
