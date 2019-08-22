from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
chrome_path = 'C:\\Users\\User\\py-scrap\\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

driver.get("https://www.google.com")
