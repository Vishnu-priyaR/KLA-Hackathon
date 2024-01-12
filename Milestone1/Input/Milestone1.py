import numpy as np 
import math
f=open("Testcase1.txt","r")
data=[]
for line in f:
    data.append(line.split(":")[1])
d,n,angle=int(data[0]),int(data[1]),int(data[2])
print(d,n,angle)
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
for i in points:
    f.write(str(tuple(i))+'\n')
f.close()