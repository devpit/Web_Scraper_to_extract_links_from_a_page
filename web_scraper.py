import requests
from bs4 import BeautifulSoup

url = "https:www.example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        print(f"Link Found: {link.get('href')}")
else:
    print(f"The solicitation is failed, status code {response.status_code}")
