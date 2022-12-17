import requests
from bs4 import BeautifulSoup 
webpage = requests.get(f'https://modship.com/')
# print(webpage)
soup = BeautifulSoup(webpage.text,'html.parser')
# print(soup.prettify())
text=soup.text
print(text)