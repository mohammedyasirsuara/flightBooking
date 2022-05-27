#Selenium
import time
from telnetlib import EC
from typing import final

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\Program Files (x86)\msedgedriver.exe")
driver = webdriver.Edge(service=PATH)

ORIGIN = 'Ottawa'
DESTINATION = 'Vancouver'
DEPARTURE = '11/07/2022'
RETURN = '05/08/2022'
NUM_PASS = '1'

def setdep():
    dep = driver.find_element(By.ID, 'bkmgFlights_travelDates_1-formfield-1')
    dep.click()
    dep.send_keys(DEPARTURE)

    arr = driver.find_element(By.ID, 'bkmgFlights_travelDates_1-formfield-2')
    arr.click()
    arr.send_keys(RETURN)
    
def main():
    try:
        driver.get("https://www.aircanada.com/ca/en/aco/home.html")

        #Select Round-Trip
        ttype = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'bkmgFlights_tripTypeSelector_R'))
        )
        ttype.click()
        
        origin = driver.find_element(By.ID, 'bkmgFlights_origin_trip_1')
        origin.send_keys(ORIGIN)
        driver.implicitly_wait(6)

        origin = driver.find_element(By.ID, 'bkmgFlights_destination_trip_1')
        origin.send_keys(DESTINATION)
        driver.implicitly_wait(6)

        setdep()
        time.sleep(2)

        print(driver.title)
        numPass = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, 'bkmgFlights_selectTravelersMainContainer'))
        )
        numPass.click()

        time.sleep(5)

    except:
        driver.quit()

main()