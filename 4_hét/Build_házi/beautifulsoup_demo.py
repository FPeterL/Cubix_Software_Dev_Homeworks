#pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup

#Cubix python képzések szűrés linkje
url = "https://courses.cubixedu.com/kepzesek?_gl=1%2a1ussfu4%2a_ga%2aMTAyMjg2NjYxNS4xNzE5MzA5ODM4%2a_ga_KG4N6G61R4%2aMTcyODQ1NDA0MS4yMS4wLjE3Mjg0NTQwNTkuNDIuMC45NDYyNDc2NTc.%2a_gcl_au%2aOTgzMjU5OTY4LjE3MjgzOTM2MzA.&tags=python"

# Az oldal alap URL-je a relatív hivatkozásokhoz
base_url = "https://courses.cubixedu.com"

# Weboldal lekérése
response = requests.get(url)

# Oldal válaszának ellenőrzése
if response.status_code == 200:
    print("Cubixon elérhető Python képzések listája:")
    # HTML feldolgozása BeautifulSouppal
    soup = BeautifulSoup(response.text, 'html.parser')

    # Képzések keresése: 'course-box-v2' osztályú elemek, amelyek <a> tageket tartalmaznak
    courses = soup.find_all('div', class_='course-box-v2')

    # Képzések URL-jeinek és a belső címek lekérése
    for course in courses:
        link = course.find('a', href=True)  # Keresünk <a> tagot href attribútummal
        if link:
            # Ellenőrizzük, hogy a link relatív-e, és ha igen, csak akkor fűzzük hozzá a base_url-t
            if link['href'].startswith('http'):
                course_url = link['href']  # Teljes URL, nincs szükség a base_url-re
            else:
                course_url = base_url + link['href']  # Relatív URL, fűzzük hozzá a base_url-t
            # Az egyes képzések oldalának lekérése
            course_response = requests.get(course_url)
            if course_response.status_code == 200:
                # Képzések oldala feldolgozása
                course_soup = BeautifulSoup(course_response.text, 'html.parser')
                # Az 'h1' elem keresése (a képzés címe)
                h1_tag = course_soup.find('h1')
                if h1_tag:
                    print(f"Képzés címe: {h1_tag.get_text().strip()}")
                    print(f"Link a képzéshez: {course_url}")
                else:
                    print("Nem található 'h1' elem az oldalon.")
            else:
                print(f"Nem sikerült elérni a képzés oldalát. HTTP hiba: {course_response.status_code}")
else:
    print(f"Nem sikerült elérni az oldalt. HTTP hiba: {response.status_code}")
