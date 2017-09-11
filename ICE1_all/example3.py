import random
x2 = random.randint(0,9)
print(x2)


x1 = int(input("enter a number :"))
if x1 == x2:
     print("perfect")
elif x1<x2:
    print("lesser")
else:
    print("greater")
