import turtle as t
import random

t.shape("triangle")
t.speed(4)

for x in range(500):
    a = random.randint(1, 360)
    t.setheading(a)
    b=random.randint(1,30)
    t.forward(b)
