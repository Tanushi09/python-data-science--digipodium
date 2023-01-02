from bs4 import BeautifulSoup
import requests

url = 'http://www.google.com/search?=css'
response = requests.get(url)
if not response.status_code == 200:
    print("An error has occured.")
    exit()
else :
    print("success")
    soup = BeautifulSoup(response.text,'html5lib')
    #get all headings
    headings_1=soup.find_all('hi')
    print("Headings 1:")
    for i in headings_1:
        print(i.text)

    headings_2 = soup.find_all('h2')
    print("Headings 2:")
    for i in headings_2:
        print(i.text)

    headings_3 = soup.find_all('h3')
    print("Headings 3:")
    for i in headings_3:
        print(i.text)

    #get all links
    links = soup.find_all('a')
    print("Links:")
    for i in links:
        print(f'{i.text}➡️ {i.get("href")}')

