#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
if direction=='encode':
  shift=shift
elif direction=='decode':
  shift*=-1
else:
  print("Invald input")
  quit()
a=len(alphabet)
l=len(text) #"Hello World!" = 12 char
t=[]
for x in range(0,l):
  t.append(text[x])
T=[] 
z=""
for x in range(0,l):
  p=t[x]
  if alphabet.count(p)==0:
    T.append(t[x])
  else:
    q=alphabet.index(t[x])
    q+=shift
    T.append(alphabet[q%a])
for x in range(0,l):
  z+=str(T[x])
if direction=='encode':
  print(f"Here's the encoded: {z}")
elif direction=='decode':
print(f"Here's the decoded: {z}")
