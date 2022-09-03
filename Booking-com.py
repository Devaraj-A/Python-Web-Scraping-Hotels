import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

driver=webdriver.Chrome('/home/deva/Documents/Spyder/Selenium/chromedriver')
driver.get('https://www.booking.com/searchresults.en-gb.html?label=gen173rf-1FCAEoggI46AdIM1gDaGyIAQGYAQm4ARnIAQzYAQHoAQH4AQuIAgGiAgxyZXNuZXh1cy5jb22oAgO4AtmsiI0GwAIB0gIkZGRkODE1OGUtMTQ0MS00ZjllLWE5NmEtZmNmNzkwNjEzYzIz2AIG4AIB;sid=84623fcabc46fad8f2bd491bf70b8249;city=-2092174;from_idr=1&;dr_ps=IDR;ilp=1;d_dcp=1')
driver.maximize_window()
soup=BeautifulSoup(driver.page_source, 'lxml')

df=pd.DataFrame({'Name':[''], 'Link':['']})
counter=0
while counter<10:
    hotel=soup.find_all('div', class_='_5d6c618c8')
    for hotels in hotel:
        name=hotels.find('div', class_='fde444d7ef _c445487e2').text
        link=hotels.find('a', class_='fb01724e5b').get('href')
        df=df.append({'Name':name, 'Link':link}, ignore_index=True)
    next_page=driver.find_element_by_xpath("//Button[@aria-label='Next page']")
    next_page.click()
    time.sleep(3)
    counter +=1
driver.close()
df.to_csv('/home/deva/Desktop/Booking.xlsx')
