from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import shutil
import os
import re

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://aiot.kaitechstudio.com/Login/")

login = 'ttu410606136'


elem = browser.find_element_by_name('userID')
elem.send_keys(login)
elem.send_keys(Keys.ENTER)

counter = ''
while True:
    counter = browser.find_element_by_id('succesCounter').text
    if counter != '':
        break

print('counter is:', counter)

while True:
    Q1 = browser.find_element_by_id('Q1').get_attribute('value')
    Q1 = Q1.replace('|', 'ttu410606136').replace(' ', '')
    
    Q2 = browser.find_element_by_id('Q2').get_attribute('value')
    Q2s = Q2.split(' ')
    if(Q2s[1] == '+'):
        Q2_answer = int(Q2s[0]) + int(Q2s[2])
    

    elif(Q2s[1] == '-'):
        Q2_answer = int(Q2s[0]) -  int(Q2s[2])
    

    elif(Q2s[1] == '*'):
        Q2_answer = int(Q2s[0]) *  int(Q2s[2])
    

    elif(Q2s[1] == '%'):
        Q2_answer = int(Q2s[0]) %  int(Q2s[2])
    
    print(Q1)
    print(Q2)
    Q1_answer = Q1
    
    browser.find_element_by_id('Q1a').send_keys(Q1_answer)
    browser.find_element_by_id('Q2a').send_keys(Q2_answer)
    browser.find_element_by_id('btnSubmit').click()
    time.sleep(0.3)
    counter = browser.find_element_by_id('succesCounter').text
    if counter == '200':
        browser.refresh()
        break

   
