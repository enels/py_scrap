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


import csv

with open("C:\\Users\\User\\py-scrap\\country_codes", "r") as country_codes:
    reader = csv.reader(country_codes)
    country_code = []

    # loops through the csv entries and appends them to a list
    for row in reader:
        country_code.append(row[1].lower())

# gets the total number of country codes in list
total_codes = len(country_code)

    
import re

# goes through each of the country for that particular query entered by the user
for index in range(0,total_codes):
    search_term = 'site:' + country_code[index] + parameters.user_query

    # navigate to the google search engine page
    driver.get("https://www.google.com")

    # locate search form by name
    search_query = driver.find_element(By.XPATH, "//input[@name='q']")

    # send_keys() to search bar
    search_query.send_keys(search_term)
    time.sleep (10)

    # hit the search button
    search_query.send_keys(Keys.RETURN)

    # wait for the browser time to load
    time.sleep (10)

    # stores the total number of mails extracted
    total_num_of_mails = 0
    
    
    with open("C:\\Users\\User\\" + parameters.filename, "w") as result:
        writer = csv.writer(result, delimiter=",")

        more_pages = True
        while more_pages == True:
            # select the classes (this helps to filter the ads away)
            linkedin_emails = driver.find_elements_by_class_name('st')

            # using python's list comprehension to filter out the mails
            linkedin_emails = [email.text for email in linkedin_emails]

            # check the number of emails found on the current page
            length = len(linkedin_emails)

            # calculate and store the over sum of emails found during the search
            total_num_of_mails = total_num_of_mails + length
            
            print("Total Number of emails in page: ", length)
            for text in  linkedin_emails:

                # extracts the mail
                email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)

                if len(email) > 1 and email[0] == email[1]:
                    # output the user's parameters to a csv file
                    writer.writerow(email[0])
                else:
                    # output the user's parameters to a csv file
                    writer.writerow(email)

                # writes to stdout
                print (text, '\n\n')

            time.sleep(10)

            try:
                driver.find_element_by_link_text("Next").click()
            except:
                print ("Error: Page not Found")
                more_pages = False
            
            #breakpoint
            
print ("Total number of linkedin emails extracted: ", total_num_of_mails)
print ("End of Search")
driver.quit()
