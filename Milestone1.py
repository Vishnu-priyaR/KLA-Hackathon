import numpy as np 
import math
d=int(input("Enter the diameter : "))
n=int(input("Enter the Number Of Points : "))
angle=eval(input("Enter the angle: "))
r = d / 2
if angle:
    angle_rad = math.radians(angle)
    x = r * math.cos(angle_rad)
    y = r * math.sin(angle_rad)
else:
    x,y=r,0
points=np.linspace(start=[-x,-y], stop=[x,y], num=n)
print(points)
f=open("output.txt","w")
x,y=[],[]
for i in points:
    f.write(str(tuple(i))+'\n')
f.close()