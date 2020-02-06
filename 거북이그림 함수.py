import turtle as t

def polygon(n,distance):
    t.shape("triangle")
    t.color("blue")
    t.pensize("2")
    t.fillcolor("grey")
    t.begin_fill()
    for i in range(n):
        t.fd(distance)
        t.lt(360/n)
    t.end_fill()
polygon(3,200)
