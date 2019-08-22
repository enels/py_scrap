from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.nytimes.com")

time.sleep(6)
headlines = driver.find_elements_by_class_name("story-heading")
if ( len(headlines) > 0 ):
    for headline in headlines:
        print(headline.text.strip())
else:
    print ("No element found")
