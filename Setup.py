
from lib2to3.pgen2 import driver
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import Running

driver = None
site = None

# Sets up the necessary variables, allowing for fewer parametres in other functions
def initiate(driver1, site1):
    global driver
    driver = driver1
    global site 
    site = site1
    Running.setup(driver1, site1)
    #print(site)

# Switches the language
def switchLanguage(newLang):
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

    __goBack()

# Goes back 
def __goBack():
    driver.back()
    driver.back()
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.COMMAND + "r")


def multilingualize():
    location = site.replace("llworkspace", "ll&objAction=EditTemplateML&objId=23190&nexturl=%2Fotcs%2Fcs%2Eexe%3Ffunc%3Dll%26objid%3D2006%26objAction%3Dbrowse%26sort%3Dname")
    driver.get(location)

    try:
        wait = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "editMLDestLang"))
        )
        Select(driver.find_element(By.ID, "editMLDestLang")).select_by_value("fr")
    except:
        print("Page wouldn't load")
        time.sleep(10)
        driver.quit()

    driver.find_element(By.NAME, "_1_1_2_Dest").send_keys("TF FR")
    driver.find_element(By.NAME, "_1_1_4_Dest").send_keys("TML FR")
    driver.find_element(By.ID, "_1_1_2").click()
    driver.find_element(By.ID, "_1_1_3").click()

    driver.find_element(By.NAME, "radTransType").click()
    driver.find_element(By.NAME, "radTransType").send_keys(Keys.RIGHT)
    driver.find_element(By.NAME, "_1_1_3_Dest_pp").clear()
    driver.find_element(By.NAME, "_1_1_3_Dest_pp").send_keys("un" + Keys.ENTER + "deux" + Keys.ENTER + "trois")
    driver.find_element(By.ID, "btnSave").click()

    try:
        wait = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "mini_public_timeline"))
        )
        goHome()
    except:
        print("Took too long to save multilingualization")


def goHome():
    driver.get(site)


def check():
    temp = input("Continue? y/n")
    temp = temp.lower()
    if (temp == "n"):
        quit = input("Quit? y/n")
        quit = quit.lower()
        if (quit == "y"): driver.quit()
        else: qwert = input("Press enter to continue")



def multilingualizeLong():
    print(site)
    admin = site.replace("llworkspace", "admin.index")
    driver.get(admin)

    try:
        wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "filter_Accordion"))
        )
        driver.find_element(By.ID, "filter_Accordion").clear()
        driver.find_element(By.ID, "filter_Accordion").send_keys("categories")
        driver.find_element(By.ID, "NavigationPane_3_6").click()
    except:
        print("Admin pages wouldn't load")
        time.sleep(5)
        driver.quit()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "x23190"))
        )
        driver.find_element(By.ID, "x23190").click()
    except:
        print("Categories volume wouldn't load")
        #driver.quit()

    driver.find_element(By.ID, "menuItem_Properties_23190").click()

    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "/otcs/cs.exe?func=ll&objAction=EditTemplateML&objId=23190&nexturl=%2Fotcs…%252526objid%25253D2006%252526objAction%25253Dbrowse%252526sort%25253Dname"))
        )
        driver.find_element(By.LINK_TEXT, "/otcs/cs.exe?func=ll&objAction=EditTemplateML&objId=23190&nexturl=%2Fotcs…%252526objid%25253D2006%252526objAction%25253Dbrowse%252526sort%25253Dname").click()
    except:
        print("BW Category wouldn't load")
        driver.quit()
    
    try:
        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "editMLDestLang"))
        )
        Select(driver.find_element(By.ID, "editMLDestLang")).select_by_value("fr")
    except:
        print("Multilingual tab wouldn't load")
        driver.quit()
    
    driver.find_element(By.NAME, "_1_1_2_Dest").send_keys("TF FR")
    driver.find_element(By.NAME, "_1_1_4_Dest").send_keys("TML FR")
    driver.find_element(By.ID, "_1_1_2").click()
    driver.find_element(By.ID, "_1_1_3").click()

    driver.find_element(By.NAME, "radTransType").click()
    driver.find_element(By.NAME, "_1_1_3_Dest_pp").clear()
    driver.find_element(By.NAME, "_1_1_3_Dest_pp").send_keys("un" + Keys.ENTER + "deux" + Keys.ENTER + "trois")
    driver.find_element(By.ID, "btnSave").click()

    try:
        wait = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Comment"))
        )
        goHome()
    except:
        print("Took too long to save multilingualization")