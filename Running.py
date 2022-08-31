from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import Setup

driver = None
site = None
num = 0

def setup(driver1, site1):
    global driver
    global site
    driver = driver1
    site = site1


def classicRun(SDL, UDL, earlyExit):
    Setup.goHome()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "node21650"))
        )
        driver.find_element(By.ID, "node21650").click()
    except:
        print("Couldn't find 'Other Items'")
    