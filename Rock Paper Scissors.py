rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pick=[rock,paper,scissors]
pick1=["rock","paper","scissors"]
print('Type "0" for rock, "1" for paper, or "2" for Scissors')
a=int(input())
import random
b=random.randint(0,2)
print(f"Computer Chose: {pick1[b]}\n",pick[b])
if 0<=a<=2:
  print(f"You Chose: {pick1[a]}\n",pick[a])
  if a==b:
    print("Draw Match\nGame Over!")
  elif a==(b-1):
    print("You lose\nGame Over!")
  elif a==2 and b==0:
    print("You lose\nGame Over!")
  else:
    print("You Win!")
else:
  print("Out of choise\nGame over!")
