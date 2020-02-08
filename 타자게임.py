import random
import time

point = 0
word_list = ["carrot",'horse','brutal','great','power','ambition']
print("준비되면 엔터키 ㄱ")
input()
start_time = time.time()

for i in range(5):
    question =random.choice(word_list)
    print(question)
    x = input("따라 쓰시오.\n")
    if question == x:
        print("Correct!")
        point = point+1
    else:
        print("잘못 썼어!")
    word_list.remove(question)

end_time = time.time()
et = end_time - start_time
et = format(et,'.2f')
if point == 5:
    print(et,'초 걸렸어요')
    print("다맞음")
else:
    print(et,'초 걸렸어요')
    print("분발혀")
