import random
from turtle import *
timmy = Turtle()
lis = ["Blue", "Red", "Green", "Brown", "Pink"]
timmy.width(0.5)
timmy.speed("fastest")
scr = Screen()
for i in range(360):
    timmy.circle(100)
    c = random.randint(0, 4)
    timmy.color(lis[c])
    timmy.left(5)
scr.exitonclick()
