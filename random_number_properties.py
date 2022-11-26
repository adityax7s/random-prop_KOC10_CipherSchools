import random
a=int(input("Enter value for A:"))
b=int(input("Enter value for B:"))
x = random.randint(a,b)
print("Range is","(",a,",",b,") and randomly picked number is",x)
print()
if x%2==0:
    print(x,"is a even number")
else:
    print(x,"is a odd number")

if x>=0:
    print(x,"is a positive integer")
else:
    print(x,"is a negative integer")


if x> 1:
    for i in range(2, x):
        if (x% i) == 0:
            print(x, "is a composite number")
            break
    else:
        print(x, "is a prime number")
elif x== 0 or 1:
    print(x, "is a neither prime NOR composite number")
else:
    print(x,"is a composite number")
