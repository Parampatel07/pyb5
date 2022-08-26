# write a program to print following series (Lucas series)
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 6000
first=2
second=1
print(first)
print(second)
answer=first+second
print(answer)
while answer<3571:
    first=answer
    answer=second+answer
    print(answer)
    second=answer
    answer=first+answer
    print(answer)