##########
#11111111111111
#2222222222222




##########
import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()

website = 'https://propertyhub.in.th/%E0%B9%80%E0%B8%8A%E0%B9%88%E0%B8%B2%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94/bts-%E0%B8%AD%E0%B9%88%E0%B8%AD%E0%B8%99%E0%B8%99%E0%B8%B8%E0%B8%8A'
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = webdriver_service, options = chrome_options)
driver.get(website)
time.sleep(5)

room_for_rent = []

for page_num in range(151):
    # Wait for the rooms to load on the current page
    wait = WebDriverWait(driver, 10)
    rooms = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'sc-152o12i-12 iHtzLg')]")))
    
    # Scrape the data for each room and append to the list
    for room in rooms:
        room_df = room.text
        room_for_rent.append({'room_for_rent': room_df})
    
    # Click the next button to navigate to the next page
    next_button = driver.find_element(By.XPATH, '//*[text()="ถัดไป"]')
    next_button.click()
    time.sleep(2) #add abit sleep

    df = pd.DataFrame({'room_for_rent': room_for_rent})

    df.to_csv('CondoOnnuch_WebScraping1.csv', index=False, encoding="utf-8-sig") #utf-8-sig for reading Thai Alphabet
#the exported data will be a sigle column, which will be splited in Power Quary as it is easier