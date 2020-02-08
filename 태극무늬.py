import turtle as t

t.bgcolor("black")
t.shape("triangle")
t.speed(0)

for x in range(500):
    if x % 3 == 0:
        t.color("red")
    if x % 3 == 1:
        t.color("blue")
    if x % 3 == 2:
        t.color("yellow")
    t.forward(x*2)
    t.left(119)
