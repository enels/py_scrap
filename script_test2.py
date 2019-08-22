""" filename: script.py """

# imports selenium
from selenium import webdriver


# import Keys
from selenium.webdriver.common.keys import Keys

# imports parameters
import parameters

# imports By
from selenium.webdriver.common.by import By

# imports parsel
from parsel import Selector

# imports time
import time

# Defining the path to the chrome driver
# driver = webdriver.Chrome(r"C:\Users\User\py-scrap\chromedriver")

options = webdriver.ChromeOptions()
options.add_argument("C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
chrome_path = 'C:\\Users\\User\\py-scrap\\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

driver.get("https://www.google.com")

# locate search form by name
search_query = driver.find_element(By.XPATH, "//input[@name='q']")

# send_keys() to search bar
search_query.send_keys(parameters.search_term)
time.sleep (5)


search_query.send_keys(Keys.RETURN)
print ("Having Problems with CAPTCHA")
driver.quit()

