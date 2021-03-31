from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import shutil
import os

def getLastestFilename():
    path = 'C:\\Users\\admin\\Downloads'  
    try:
        filename = max([f for f in os.listdir(path)],\
            key = lambda x: os.path.getmtime(os.path.join(path,x)))
    except:
        filename = max([f for f in os.listdir(path)],\
            key = lambda x: os.path.getmtime(os.path.join(path,x)))
    return filename

def changeName(finalname):
    while True:
        filename = getLastestFilename()
        if filename.endswith('.csv'):
            break
    path = 'C:\\Users\\admin\\Downloads'    
    shutil.move(f'{path}\\{filename}',f'{path}\\{finalname}')

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://e-service.cwb.gov.tw/HistoryDataQuery/")

while True:
    try:
        browser.find_element_by_id("Button_North").click()
        break
    except:
        pass


for item in Select(browser.find_element_by_id('stationCounty')).options:
    print(item.text)
    if item.text.find('新北市') != -1:
        Select(browser.find_element_by_id('stationCounty'))\
            .select_by_visible_text(item.text)

for item in Select(browser.find_element_by_id('station')).options:
    Select(browser.find_element_by_id('station'))\
        .select_by_visible_text(item.text) 


    browser.find_element_by_id('datepicker').send_keys('2021-03-22')
    browser.find_element_by_id('doquery').click()

    windows = browser.window_handles
    browser.switch_to_window(windows[-1])
    browser.find_element_by_xpath("//input[@src='images/downloadCSV_2.png']").click()
    browser.close()
    browser.switch_to_window(windows[0])
    time.sleep(1) 
    changeName(f"{item.text}.csv")

    break