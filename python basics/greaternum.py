a=int(input("num 1 "))
b=int(input("num 2 "))
c=int(input("num 3 "))
if a>b and a>c:
    print(a,"is greater")
elif b>c and b>a:
    print(b,"is greater")
elif c>a and c>b:
    print(c,"is greater")
else:
    print("invalid numbers")
