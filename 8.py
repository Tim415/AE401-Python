import turtle
import random
t=turtle.Turtle()
turtle.colormode(255)
x=-80
y=-80
t.speed(100)
for n in range(8):
    for m in range(7):
        t.penup()
    t.color(random.randint(0,255),random.randint(0,255),random(0,255))
        t.goto(x,y)
        t.dot(10)
        x=x+30
    x=-80
    y=y+30