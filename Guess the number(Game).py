#Guess the number
print("   Welcome to Number Guessing Game\n")
import random
lis=[]
a = random.randint(0,100)
i =input('Chose the difficulty level:\nPress "H" for hard:\nPress "M" for Medium\nPress "E" for Easy:\n').lower()
if i=="h":
  Lives=5
elif i=="m":
  Lives=7
elif i=="e":
  Lives=10
else:
  print("Game Over!")
  exit()
while Lives!=0:
  print(f"Lives remaining: {Lives}")
  b=int(input('Guess a number from "0" to "100": '))
  lis.append(b)
  if a==b:
    print("You Win!")
    break
  elif a-b==1 or b-a==1:
    print("You are too near")
  elif a-b<0:
    print("You guess too high")
  elif a-b>0:
    print("You guess too low")
  else:
    print("You are aproaching")
  print(lis)
  if lis.count(b)>1:
    pass
  else:
    Lives-=1
