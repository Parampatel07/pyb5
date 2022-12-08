import random

number=[10,20,30,40,50,60,80,70]
answer = random.random()
print(answer)

answer =random.uniform(50,100)
print(answer)

answer=random.randint(1,25)
print(answer)

answer=random.randrange(10,100,5)
print(answer)

answer = random.choice(number)
print(answer)

answer = random.choices(number,k=3)
print(answer)