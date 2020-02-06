import random
a = random.randint(0,100)
b = random.randint(0,100)
print(a,"+",b,"=")
c = input()
c = int(c)

if c == (a+b):
    print("good!")
else:
    print("not good!")
