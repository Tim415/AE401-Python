import turtle
turtle.shape('turtle')
turtle.penup()
size=20
for i in range(70):
    turtle.stamp()
    size=size+2
    turtle.forward(size)
    turtle.right(24)
turtle.done()