word_list = ["aardvark", "banana", "baboon", "camel"]
import random
a = random.choice(word_list)
b, c, d = len(a) [], []
for x in range(0,b):
  c.append(a[x])
  d.append("_")
print(f"You only have {b+1} lifes.")
for x in range(0,b+1):
  if d.count("_") == 0:
    print("\n   You win!")
    exit()
  i = input("\nGuess a letter: ").lower()
  for k in range(0,b):
    if c[k] == i:
      d[k] = i
    print(d[k],end=" ")
if d.count("_") != 0:
  print("\nOut of lives!\n    Game Over!")
else:
  print("\n   You win!")
