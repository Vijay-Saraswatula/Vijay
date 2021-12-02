# Turtle Racing without Threads
from turtle import *
import random


def fun(obj, col, y):
    obj = Turtle()
    obj.shape("turtle")
    obj.penup()
    obj.color(col)
    obj.setx(-250)
    obj.sety(y)
    return obj


scr = Screen()
bet_colour = scr.textinput(title="Turtle Race", prompt="Pick a colour(red/yellow/green/blue/pink/orange): ").lower()
tim1 = fun("tim1", "red", 150)
tim2 = fun("tim2", "yellow", 100)
tim3 = fun("tim3", "green", 50)
tim4 = fun("tim4", "blue", 0)
tim5 = fun("tim5", "pink", -50)
tim6 = fun("tim6", "orange", -100)
t1, t2, t3, t4, t5, t6 = [], [], [], [], [], []
dic = {tim1: t1, tim2: t2, tim3: t3, tim4: t4, tim5: t5, tim6: t6}
lis = [tim1, tim2, tim3, tim4, tim5, tim6]
t = True
while t:
    for i in lis:
        a = random.randint(0, 10)
        i.forward(a)
        dic[i].append(a)
        if sum(dic[i]) >= 500:
            t = False
            Col = str(i.color()[1])
            break
print(f"Your Input: {bet_colour}, Winner: {Col}")
print(f"Turtle scores(in mm): ", sum(t1), sum(t2), sum(t3), sum(t4), sum(t5), sum(t6))
if bet_colour == Col:
    print(f"You Win! {Col} is the winner!")
else:
    print(f"You Lost! {Col} is the winner!")
scr.exitonclick()
