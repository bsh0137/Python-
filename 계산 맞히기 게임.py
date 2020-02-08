import random

def make_question():
    a = random.randint(1,3)
    b = random.randint(1,100)
    c = random.randint(1,100)
    if a == 1:
        b = str(b)+'+'
    elif a == 2:
        b = str(b)+'-'
    elif a== 3:
        b = str(b)+'*'
    b = b+str(c)
    return b

point = 0

for i in range(5):
    d = make_question()
    print(d)

    print("정답은?")
    x = int(input())

    if x == eval(d):
        print('good!')
        point = point +1
    else:
        print("incorrect!")

print("정답 개수:",point,"오답 개수:",5-point)

if point ==5:
    print("You are genius")
elif point >=3:
    print("good!")
elif point >=1 :
    print("not bad!")
elif point == 0:
    print("Your head is useless")
    
