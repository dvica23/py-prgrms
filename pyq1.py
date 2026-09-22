n=int(input())
k=int(input())
j=int(input())
m=int(input())
p=int(input())
if n<=0 or k<=0 or j<=0 or m<0 or p<0:
  print("Invalid Input")
else:
    banana=m//k
    peanut=p//j
    eaten=banana+peanut
    remaining=n-eaten
    if remaining<0:
      remaining=0
    print("Number of monkeys left on the tree:",remaining)
