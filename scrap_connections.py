import getpass
import requests
import time
import pprint
import random
import re
import html5lib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.common import exceptions
import parameters

# initialize variable to store username/email and password
userid = str(input("Enter email address: "))

user_pass = getpass.getpass()

# Defining the path to the chrome driver
driver = webdriver.Chrome(parameters.chrome_path)

# launch the linkedin website
driver.get("https://www.linkedin.com")

# go for another 0.2 seconds break again
time.sleep (0.2)

# Locate email form by class name
username = driver.find_element_by_class_name('input__field--with-label')


# Send the usernmae to the chrome browser
username.send_keys(userid)

# Locate password by class name
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

# Send password to the chrome driver
password.send_keys(user_pass)

# go for another 0.5 seconds break again
time.sleep (0.5)

# select the sign in button
sign_in_button = driver.find_element_by_class_name("sign-in-form__submit-btn")

# mimic clicking on the sign in button
sign_in_button.click()

# wait for page to load
time.sleep (0.5)

driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")

#total_height = driver.execute_script("return document.body.scrollHeight")

print ("Gathering Connections")

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
page_count = 1
match=False
while(match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True
    
page = bs(driver.page_source, "html5lib")

# get all the connection class
content = page.find_all('a', {'class':'mn-connection-card__link ember-view'})

# Debugging code
"""print (content)
print (content2)"""

# container for storing the connections
mynetwork = []

# asks user where to begin collecting the connectionns
index = int(input("Begin from: "))

# get all the 
for contact in content[index:]:
    mynetwork.append(contact.get('href'))

print(len(mynetwork), " connections found\n")

# for storing the extracted network emails
my_network_emails = []

print ("Extraction Started:\n=================\n")
print ("Wait for a while wihle the program performs its magic\n")

mail_count = index
# connect to the profile of all contacts and save the email within a list
for contact in mynetwork:
    driver.get("https://www.linkedin.com" + contact + "detail/contact-info/")
    driver.implicitly_wait(3)
    contact_page = bs(driver.page_source, "html5lib")
    content_contact_page = contact_page.find_all('a', href=re.compile('mailto'))

    for contact in content_contact_page:
        print(mail_count, contact.get('href')[7:])
        my_network_emails.append(contact.get('href')[7:])
        mail_count += 1
        #print(mail_count)

    time.sleep(random.uniform(0.5, 1.9))
    
# opens the file to store the connection emails
fh = open("C:\\Users\\Edobor\\connection_emails.txt", "w")

# iterates through the collected emails list and stores it in a file
for email in my_network_emails:
    email = str(email)
    fh.write(email + "\n")

fh.close()
print ("Extraction Successfully Complete!!")
# Connect to the profile of all the contacts and save the profile within a list
#for contact in mynetwork:

