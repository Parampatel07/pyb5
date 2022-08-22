# example of dict.
books={'name':'atomic habit','price':4500,'pages':450,'author':'bj franklin'}
name={'name':'param patel','age':17}
print(books)

print(books['name'])
books['price']=5000
print(books)

# books.clear()
print(books)

temp=books.copy()
print(temp)

temp=books.items()
print(temp)

temp=books.keys()
print(temp)

temp=books.pop('author')
print(temp)

temp=books.popitem()
print(temp)

books.update(name)
print(books)

temp=books.values()
print(temp)