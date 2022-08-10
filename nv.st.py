from time import sleep

from click import option
from params import credentials
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from details import details

url = 'https://christembassysoultracker.org/'

options = Options()
# options.headless = True
options.add_argument('--start-maximized')

browser = webdriver.Chrome(options=options)
browser.get(url)

def login():
    browser.find_element(By.CSS_SELECTOR, "#loginUsername").send_keys(credentials['username'])
    browser.find_element(By.CSS_SELECTOR, '#loginPassword').send_keys(credentials['password'])
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#logText").click()

while browser.current_url != f"https://www.christembassysoultracker.org/soul":
    login()
else:
    print("Logged in")

for detail in details:
    first_name = detail['firstName'].title()
    last_name = detail['lastName'].title()
    gender = detail['gender'].title()
    phone_number = '0' + detail['phoneNumber']


    FirstName = browser.find_element(By.CSS_SELECTOR, '#soul_firstname')
    FirstName.clear()
    FirstName.send_keys(first_name)
    # browser.find_element(By.CSS_SELECTOR, '#soul_firstname').send_keys(first_name)
    

    LastName = browser.find_element(By.CSS_SELECTOR, '#soul_lastname')
    LastName.clear()
    LastName.send_keys(last_name)
    # browser.find_element(By.CSS_SELECTOR, '#soul_lastname').send_keys(last_name)



    Select(browser.find_element(By.CSS_SELECTOR, '#soul_gender')).select_by_value(gender)

    City = browser.find_element(By.CSS_SELECTOR, '#soul_city')
    City.clear()
    City.send_keys('Lagos')
    # browser.find_element(By.CSS_SELECTOR, '#soul_city').send_keys('Lagos')

    Select(browser.find_element(By.CSS_SELECTOR, '#soul_country_code')).select_by_value('NG')


    PhoneNumber = browser.find_element(By.XPATH, '//*[@id="soul_phoneno"]')
    PhoneNumber.clear()
    PhoneNumber.send_keys(phone_number)
    # browser.find_element(By.XPATH, '//*[@id="soul_phoneno"]').send_keys(phone_number)


    sleep(1)
    browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    browser.find_element(By.CSS_SELECTOR, '#logText').click()

    try:
        message = browser.find_element(By.CSS_SELECTOR, '#submit_feedback > div > span').text
        if message != 'Successfully Added.':
            print(message)
            # browser.refresh()
            FirstName.clear()
            LastName.clear()
            City.clear()
            PhoneNumber.clear()
            continue
        else:
            print(f"{first_name} {last_name} has been added succesfully")
    except NoSuchElementException:
        print('Element Not Found')
