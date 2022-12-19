import requests
from bs4 import BeautifulSoup 
def get_text_from_url(url):
    webpage = requests.get(url)
    # print(webpage)
    soup = BeautifulSoup(webpage.text,'html.parser')
    # print(soup.prettify())
    # text=soup.text
    return soup
city= str(input("Enter name of city to find price "))
my_url = f'''https://www.bankbazaar.com/fuel/petrol-price-{city}.html'''
webpage = get_text_from_url(my_url)
# print(webpage)
price = webpage.find('strong',{'class':'bigfont'})
print(price.get_text())