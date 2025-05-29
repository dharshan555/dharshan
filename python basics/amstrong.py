num=int(input())
digit=len(str(num))
org=num
am=0
for i in len(str(num)):
    x=num%10
    am+=x**digit
    num//=10
if org == am:
    print(org,"is amstrong number")
else:
    print(org,"is not amstrong number")
