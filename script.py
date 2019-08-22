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
driver = webdriver.Chrome(r"C:\Users\User\py-scrap\chromedriver")

# specifies the path to the chromedriver
#driver = webdriver.Chrome(r"C:\Users\enoma\chromedriver")

# driver.get() helps navigate to the page of the given URL
driver.get("https://www.linkedin.com")

# Locate email form by class name
username = driver.find_element_by_class_name('input__field--with-label')

# Send the username to the chrome browser
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
time.sleep(0.5)

# Locate password by class name
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

# Send the password to the chrome browser
password.send_keys(parameters.linkedin_password)

# go for another 0.5 seconds break again
time.sleep (0.5)

# select the sign in button
sign_in_button = driver.find_element_by_class_name("sign-in-form__submit-btn")

# mimic clicking on the sign in button
sign_in_button.click()
time.sleep (0.5)

# if there's a page to put in your phone number execute uncomment the following lines of code
# phone_no_skip_button = driver.find_element_by_class_name('secondary-action')

# phone_no_skip_button.click()

# navigate to the google search engine page
driver.get("https://www.google.com")

# locate search form by name
search_query = driver.find_element(By.XPATH, "//input[@name='q']")

# send_keys() to search bar
search_query.send_keys(parameters.search_term)
time.sleep (3)

# hit the search button
search_query.send_keys(Keys.RETURN)

# wait for the browser time to load
time.sleep (3)

# select the green links (excluding the ads)
linkedin_urls = driver.find_elements_by_tag_name('cite')

""" Debuggin code """
"""
 check the length
 length = len(linkedin_urls)
 print(length)

if the length is more than 1 (at least 12) code is working"""
""" end """
# select the classes (this helps to filter the ads away)
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# check the length again
# print(length)
# length = len(linkedin_urls)

linkedin_urls = [url.text for url in linkedin_urls]
time.sleep (0.5)

# iterate over each url in the list
for linkedin_url in linkedin_urls:

	# get the profile url
	driver.get(linkedin_url)

	# wait 5 seconds for loading url
	time.sleep (5)

	# assign the source code for the webpage to variable sel
	sel = Selector (text=driver.page_source)

# xpath to extract text from the class containing the name
name = sel.xpath('//*[starts-with(@class,"inline")]/text()').extract_first()

# remove the newline char and spaces
if name:
	name = name.strip()

# xpath to extract the career from the class containing the career
career = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal")]/text()').extract_first()

# remove the newline char and spaces
if career:
	career = career.strip()

# xpath to extract the college from the class containing the class
#college = sel.xpath('//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()')

# remove the newline char and spaces
#if college:
	#college = college.strip()

# extract the current url of the user
linkedin_url = driver.current_url

# prints results to the terminal
print ("\n")
print ("Name: " + name)
print ("Career: " + career)
#print ("College: " + college)
print ("Linkedin url: " + linkedin_url)
print ("\n")

# imports csv
import csv
with open("C:\\Users\\User\\" + parameters.filename, "w") as result:

	writer = csv.writer(result, delimiter=",")

	# writerow() method to write to the file
	writer.writerow(['Name', 'Job title', 'Company', 'College', 'Location', 'email', 'URL'])\

	# output the user's parameters to a csv file
	writer.writerow([name.encode('utf-8'),
				
				career.encode('utf-8'),
				linkedin_url.encode('utf-8')])

# terminates the application
driver.quit()
