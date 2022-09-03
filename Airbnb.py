from database import cursor,conn
from bs4 import BeautifulSoup
import requests

url = 'https://www.airbnb.co.in/s/Paris/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Paris&place_id=ChIJD7fiBh9u5kcRYJSMaMOCCwQ&checkin=2022-04-09&checkout=2022-04-10&source=structured_search_input_header&search_type=autocomplete_click'
response = requests.get(url)

extract = BeautifulSoup(response.text, 'lxml')
ID = 0
while True:
    hotels = extract.find_all('div', class_='_gig1e7')
    for hotel in hotels:
        try:
            name = hotel.find('span', class_='ts5gl90 tl3qa0j t1nzedvd dir dir-ltr').text
            description = hotel.find('div', class_='i1wgresd dir dir-ltr').text.strip()
            rating = hotel.find('span', class_='rpz7y38 dir dir-ltr').text
            price = hotel.find('span', class_='_tyxjp1').text
            link = hotel.find('a', class_='l8au1ct dir dir-ltr').get('href')
            link_full='https://www.airbnb.co.in'+link

        except:
            pass
        ID += 1
        #cursor.execute("Truncate table")
        data = "Insert into hotels(ID, Name, Description, Rating, Price, Ref_url)Values(?,?,?,?,?,?)"
        insert = [ID,name,description,rating,price,link_full]
        cursor.execute(data,insert)
        conn.commit()
        print(ID,name,description,rating,price,link_full)
    
    next_page =extract.find('a', {'aria-label':'Next'}).get('href')
    next_full = 'https://www.airbnb.co.in'+ next_page

    response = requests.get(next_full)
    extract = BeautifulSoup(response.text, 'lxml')
