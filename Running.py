#from asyncio.streams import _ClientConnectedCallback
from lib2to3.pgen2 import driver
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#import time
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
    global num
    num += 1

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "node21650"))
        )
        driver.find_element(By.ID, "node21650").click()
    except:
        print("Couldn't find 'Other Items'")
        Setup.check()
    
    try:
        wait = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "node25060"))
        )
        driver.find_element(By.ID, "node25060").click()
    except:
        print("Couldn't find BW folder")
        Setup.check()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "addItemMenu0Head"))
        )
        driver.find_element(By.ID, "addItemMenu0Head").click()
        driver.find_element(By.ID, "menuItem_848").click()
    except:
        print("Couldn't find Business Workspace")
        Setup.check()

    try:
        wait = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "nameGlobal"))
        )
        driver.find_element(By.ID, "nameGlobal").click()
    except:
        print("Business Workspace creation wouldn't load")
        Setup.check()

    driver.find_element(By.ID, "meta_name_en_US").clear()

    if (SDL):
        string = "BW " + str(num)
        driver.find_element(By.ID, "meta_name_en_US").send_keys(string + " EN")
        driver.find_element(By.ID, "ui-id-2").click()
        driver.find_element(By.ID, "meta_comment_en_US").send_keys(string + Keys.ENTER + "EN")

    if (UDL):
        driver.find_element(By.ID, "ui-id-1").click()
        driver.find_element(By.ID, "meta_name_fr").send_keys(string + " FR")
        driver.find_element(By.ID, "ui-id-2").click()
        driver.find_element(By.ID, "meta_comment_fr").send_keys(string + Keys.ENTER + "FR")
        
    driver.find_element(By.ID, "meta_comment_ja_JP").send_keys(Keys.TAB + Keys.ENTER)
    driver.find_element(By.NAME, "Next").click()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "_1_1_2_1Global"))
        )
        driver.find_element(By.ID, "_1_1_2_1Global").click()
    except:
        print("BW Metadata didn't load")
        Setup.check()

    if (SDL):
        driver.find_element(By.ID, "mle__1_1_2_1_en_US").clear()
        driver.find_element(By.ID, "mle__1_1_2_1_en_US").send_keys("EN " + str(num))
    
    if (UDL):
        driver.find_element(By.ID, "mle__1_1_2_1_fr").send_keys("FR " + str(num))
    
    driver.find_element(By.ID, "mlEditBtnSave").click()
    
    try:
        Select(driver.find_element(By.ID, "_1_1_3_1")).select_by_value("three")
    except:
        Select(driver.find_element(By.ID, "_1_1_3_1")).select_by_value("trois")
    
    if (num <= 10):
        driver.find_element(By.ID, "_1_1_4_1").send_keys("TML" + Keys.ENTER + "FR" + Keys.ENTER + "Not multilingual")
    else:
        driver.find_element(By.ID, "_1_1_4_1").send_keys("TML" + Keys.ENTER + "EN" + Keys.ENTER + "Not multilingual")
    
    if (not earlyExit):
        driver.find_element(By.NAME, "Next").click()
        try:
            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "selected_23081"))
            )
        except:
            print("Last part of BW wouldn't load")
            Setup.check()
        
    driver.find_element(By.ID, "FinishButton").click()


    try:
        wait = WebDriverWait(driver, 20).until(
           EC.presence_of_element_located((By.NAME, "BUTTON"))
        )
    except:
        if(num)
