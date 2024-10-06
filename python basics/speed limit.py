speed=int(input("enter speed : "))
speedlimit=70
excessspeed=130
kmperpoint=5
point=0
if speed<=speedlimit:
    print("safe speed")
else:
    point=(speed-speedlimit)/kmperpoint
print(point)
if point>10:
    print("license suspended.")