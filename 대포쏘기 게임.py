import turtle as t
import random

t.shape("turtle")
t.speed(0)

t.penup()
t.goto(-1000,0)
t.pendown()
t.goto(1000,0)
t.penup()
t.goto(0,1000)
t.pendown()
t.goto(0,-1000)

def up():
    t.left(3)

def down():
    t.right(3)

def fire():
    t.forward(dist)
    if t.distance(x,y) <= 10:
        print("명중")
        t.home()
    else:
        print("안맞았지롱!")
        t.home()




t.color("blue")
t.penup()
x = random.randint(-10,10)*20
y = random.randint(-10,10)*20
t.goto(x,y)
t.pendown()
t.circle(4)
t.penup()
t.goto(0,0)
t.pendown()
dist = (x**2+y**2)**0.5



t.speed(2)
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(fire,"space")
t.listen()


