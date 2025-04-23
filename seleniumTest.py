from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

service = Service(executable_path= "/Users/jhonlloydcabahug/Testing/chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://google.com")

searchBar = driver.find_element(By.NAME, "q")
searchBar.send_keys ("Facebook" + Keys.ENTER)

time.sleep(10)

driver.quit()