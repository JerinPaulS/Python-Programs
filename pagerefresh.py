from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://selfregistration.cowin.gov.in/appointment')
while True:
    time.sleep(20)
    driver.refresh()
driver.quit()