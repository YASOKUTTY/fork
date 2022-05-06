from selenium import webdriver

driver=webdriver.Firefox()
driver.get('https://www.youtube.com/')
driver.switch_to.new_window('tab')
driver.get('https://www.saucedemo.com/')