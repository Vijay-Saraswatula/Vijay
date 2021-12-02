#Musical Chairs
n=int(input("Enter number of chairs: "))
print("Enter Chair Numbers:")
arr=[]
lis=[]
for i in range(0,n):
  arr.append(int(input()))
c=arr.copy()
x=int(input("Enter the min. chair number value: "))
for i in range(0,n):
  for j in range(0,n):
    if arr[j]<=x:
      arr.pop(j)
      arr.append(0)
    else:
      arr.append(arr[j]-x)
      arr.pop(j)
      lis.append(c[j])
l=len(lis)
print(f"Chair number {lis[l-1]} is the winner")
