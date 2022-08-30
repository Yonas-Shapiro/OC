
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def switchLanguage(driver, newLang, site):
    settings = site.replace("llworkspace", "personal.settings")
    driver.get(settings)
    
    try:
        lang = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "metadataLang"))
        )
    finally:
        if(newLang.lower() == "fr"): val = "fr"
        elif(newLang.lower() == "de"): val = "de"
        else: val = "en_US"
    
    Select(driver.find_element(By.ID, "metadataLang")).select_by_value(val)

    driver.find_element(By.CLASS_NAME, "saveButton").click()

    __goBack(driver)


def __goBack(driver):
    driver.back()
    driver.back()
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.COMMAND + "r")