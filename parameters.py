"""
	filename: parameter.py
	contents: contains all the parameters to be used by script.py
"""
# path to the chrome driver
# this will differ in your system
chrome_path = r"C:\Users\Edobor\py-scrap\chromedriver"

# path to country code file
country_codes = "C:\\Users\\Edobor\\py-scrap\\country_codes"
# email of the linkedin account
linkedin_username = "users-email-address-goes-in-here"

# password of the account
linkedin_password = "users-passwrod-goes-in-here"

# file to store the user datas
filename = "user_datas.csv"

# user defined query (this value should always change)
queries = ['.linkedin.com/pub/ "Builders" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Architect" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "CEO" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Engineer" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Manager" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Photographer" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com" OR "@qq.com" OR "@msn.com")',
           '.linkedin.com/pub/ "Agriculture" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Graphics Designer" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Sailor" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Painter" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Musician" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Singer" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com" OR "@qq.com")',
           '.linkedin.com/pub/ "Secretary" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Constructor" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Sales Manager" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Real Estate" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "Pilot" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com")',
           '.linkedin.com/pub/ "CTO" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com" OR "@qq.com")',
           '.linkedin.com/pub/ "Hotel Manager" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com" OR "@qq.com")',
           '.linkedin.com/pub/ "Photographer" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com" OR "@qq.com")',
           '.linkedin.com/pub/ "Photographer" ("@gmail.com" OR "@yahoo.com" OR "@hotmail.com" OR "@qq.com")',
           'linkedin.com/pub/ "gmail.com" OR "yahoo.com" OR "ymail.com" OR "msn.com" OR "hotmail.com" OR "mac.com" OR "ovimail.com" OR " AND "sales manager"',
           'linkedin.com/pub/ "gmail.com" OR "yahoo.com" OR "ymail.com" OR "msn.com" OR "hotmail.com" OR "mac.com" OR "ovimail.com" OR " AND "marketing"',
           'linkedin.com/pub/ "gmail.com" OR "yahoo.com" OR "ymail.com" OR "msn.com" OR "hotmail.com" OR "mac.com" OR "ovimail.com" OR " AND "director"',]

######### NB: This pattern begins every google reCaptcha page #####
pattern = '^https:\/\/www.google.com\/sorry\/index\?continue'


