from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from itertools import count
#action chains helps us in interacting with low level action eg mouse movements and perform actions when perform()is fired
from selenium.webdriver.common.action_chains import ActionChains
import time

chromedriver_path = 'C:/Users/Joe Kahora/Downloads/chromedriver.exe'
browser = webdriver.Chrome(executable_path = chromedriver_path)
browser.get('https://www.instagram.com/accounts/login')
time.sleep(5)

#type your username and password
username = browser.find_element_by_name('username')
username.send_keys('')
password = browser.find_element_by_name('password')
password.send_keys('')

#get the css selector of the login button and click it
button_login = browser.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4)')
button_login.click()
time.sleep(10)

#turn off notnow notification
notnow = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
notnow.click()
time.sleep(20)

love = browser.find_elements_by_class_name('fr66n')

for l in list(range(10)):
    love = browser.find_elements_by_class_name('fr66n')
    actions = ActionChains(browser)
    actions.move_to_element(love[l])
    actions.click(love[l])
    actions.perform()