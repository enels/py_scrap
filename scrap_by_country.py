""" filename: script.py """

# imports selenium
from selenium import webdriver

# imports selenium
import parameters

# import the NoSuchElementException error
from selenium.common.exceptions import NoSuchElementException

# import the Keys
from selenium.webdriver.common.keys import Keys

# imports By
from selenium.webdriver.common.by import By

# imports parsel
from parsel import Selector

# imports time
import time

# imports re for regex
import re


#sets the proxy server ip address
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=173.249.35.163:10010')

# Defining the path to the chrome driver
driver = webdriver.Chrome(r"C:\Users\Edobor\py-scrap\chromedriver")

# specifies the path to the chromedriver
#driver = webdriver.Chrome(r"C:\Users\enoma\chromedriver")

n = 0

import csv

with open(parameters.country_codes, "r") as country_codes:
    reader = csv.reader(country_codes)
    # stores the country codes
    country_code = []

    # stores the country names
    country_name = []

    

    # loops through the csv entries and appends them to a list
    for row in reader:
        country_name.append(row[0])
        country_code.append(row[1].lower())
        print (n+1,"-", country_name[n])
        n += 1
        
search_more = True

while search_more == True:

    # user enters the number of the country in the list
    list_num = int(input("Enter a country number: "))
    print (country_code[list_num - 1])
    cc = country_code[list_num - 1]

    # get the length of the queries
    len_of_queries = len(parameters.queries)

    # initialize the query index
    query = 0

    # loop through the queries
    # query counter
    query_counter = 0
    query_length = len(parameters.queries)
    
    for query in parameters.queries:
        search_term = "site:" + cc + query
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

        # assumes the next button on search page is always present at first hit
        next_button = True
    
        with open("C:\\Users\\Edobor\\" + parameters.filename, "w") as result:
            writer = csv.writer(result, delimiter=",")

            # assumes at least one page will be displayed on the search
            more_pages = True

            # loops through each pages
            while more_pages == True:

                time.sleep(5)
            
                # script continues after captcha has been completed successfully
                # select the classes (this helps to filter the ads away)
            
                linkedin_emails = driver.find_elements_by_class_name('st')
                

                # using python's list comprehension to filter out the mails
                linkedin_emails = [email.text for email in linkedin_emails]

                # check the number of emails found on the current page
                length = len(linkedin_emails)

                # calculate and store the over sum of emails found during the search
                total_num_of_mails = total_num_of_mails + length
            
                print("Total Number of emails in page: ", length)

                # loops through each email
                for text in  linkedin_emails:

                    # extracts the mail
                    email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)

                    # checks to avoid duplicates
                    if len(email) > 1 and email[0] == email[1]:
                        # output the user's parameters to a csv file
                        writer.writerow(email[0])
                    else:
                        # output the user's parameters to a csv file
                        writer.writerow(email)

                    # writes to stdout
                    print (text, '\n\n')

                time.sleep(10)

                # go to the next page of the search result
                try:
                    driver.find_element_by_link_text("Next").click()
                
                except NoSuchElementException:
                    # when it gets beyond the very last page
                    # or when google's recaptcha shows up
                    next_button = False

                if next_button == False:
                    # checks if the error (not finding the next page button) is
                    # due to google's recaptcha
                    url_string = driver.current_url

                    # checks if the pattern matches the start of the url string
                    result_match = re.search(parameters.pattern, url_string)

                    # checks if a pattern was found
                    if result_match != None and len(result_match[0]) > 0:
                        print ("Please fill in the google captcha, you've got 5 mins")
                        time.sleep(300)
                        next_button = True

                    # checks if the query has gotten to the end
                    if query_counter < query_length:
                        more_pages = False
                        continue
                    else:
                        print ("Search More? ")
                        answer = input("Enter 'Y' or 'N': ")
                        if answer == 'N' or answer == 'n':
                            driver.quit()
                        else:
                            more_pages = False
                    
                    
print ("Total number of linkedin emails extracted: ", total_num_of_mails)
print ("End of Search")
driver.quit()
