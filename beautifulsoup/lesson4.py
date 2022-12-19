from function import get_text_from_url,replace_values

soup = get_text_from_url("""https://www.fifaratings.com/players""")
# print(soup.prettify())

data_html  = soup.find_all('div',{'class':'entries'})
# print(data)

for i in data_html:
    data_text = i.text
    # print(data_text)
data_text2=[]   
# print(data_text)
for letter in data_text:
    if letter=='|':
        letter=''
    data_text2.append(letter)

# print(data_text2)
data_text3=''
for i in data_text2:
    data_text3 += i
print(data_text3)
data_text3 = data_text3.split(" ")
# print(data_text3)
data_text3=replace_values(data_text3,"",0)
print(data_text3)
data_text3=data_text3.remove(0)
print(data_text3)