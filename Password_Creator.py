#Password Generator
import random


def fun(list_name, l, k):
  for i in range(k):
    p = random.randint(0, len(list_name))
    l.append(list_name[p - 1])
  return l


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
a = int(input("How many letters would you like in your password?\n")) 
b = int(input(f"How many symbols would you like?\n"))
c = int(input(f"How many numbers would you like?\n"))
x, y, z = [], [], []
x = fun(letters, x, a)
y = fun(symbols, y, b)
z = fun(numbers, z, c)
pin=x+y+z
random.shuffle(pin)
Len=len(pin)
for i in range(0,Len):
  print(pin[i],end="")
