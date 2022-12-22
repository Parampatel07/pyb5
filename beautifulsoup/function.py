from bs4 import BeautifulSoup
import requests
def get_text_from_url(url):
    webpage = requests.get(url)
    # print(webpage)
    soup = BeautifulSoup(webpage.text,'html.parser')
    # print(soup.prettify())
    # text=soup.text
    return soup


def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

def divide_parts(name_of_list, size_of_part):
    # looping till length l
    for i in range(0, len(name_of_list), size_of_part):
        yield name_of_list[i:i + size_of_part]