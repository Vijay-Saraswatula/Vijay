#Damien Hirst Paintings
from turtle import *
import colorgram


def fun():
    timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)
    timmy.pendown()


lis = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    lis.append(color.rgb)
print(lis)
timmy = Turtle()
timmy.width(100)
scr = Screen()
for i in range(1, 101):
    timmy.dot(20, "red")
    timmy.penup()
    timmy.forward(50)
    if i % 10 == 0:
        fun()
scr.exitonclick()
