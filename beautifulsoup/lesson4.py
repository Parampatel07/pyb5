from function import get_text_from_url,replace_values,divide_parts

soup = get_text_from_url("""https://www.fifaratings.com/players""")
# print(soup.prettify())

data_html  = soup.find_all('div',{'class':'entries'})
# print(data)

data_text2=[]   
for i in data_html:
    data_text = i.text
    for letter in data_text:
        if letter=='|':
            letter=''
        data_text2.append(letter)
        data_text3=''
        for i in data_text2:
            data_text3 += i
        # print(data_text3)
        data_text3 = data_text3.split(" ")
        data_text3=replace_values(data_text3,"",0)
        # print(data_text3)
        data_4=[]
        for i in data_text3:
            if isinstance(i,str)==True:
                data_4.append(i)
# print(data_4)
answer=list(divide_parts(data_4,4))
print(answer)