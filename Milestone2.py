#d=int(input("Enter the Wafer diameter : "))
#s=int(input("Enter the Die Size : "))
#shift=eval(input("Enter the Die shift vector : "))
#r=eval(input("Enter the Reference Die : "))
import math
d,s,shift,r=2,1,(0,0),(15,15)
r=d/2
max_llc=(-r,-r)
llc=[]
val=int(r)
for i in range(-d,d,s):
    for j in range(-val,val,s):
        print(i,j)
        #print(math.sqrt((i+s - shift[0]) ** 2 + (j+s - shift[1]) ** 2))
        if math.sqrt((i - shift[0]) ** 2 + (j - shift[1]) ** 2) <=r:
            llc.append((i,j))
            break
        if math.sqrt((i - shift[0]) ** 2 + (j+s - shift[1]) ** 2) <=r:
            llc.append((i,j))
            break
        if math.sqrt((i+s - shift[0]) ** 2 + (j - shift[1]) ** 2) <=r:
            llc.append((i,j))
            break
        if math.sqrt((i+s - shift[0]) ** 2 + (j+s - shift[1]) ** 2) <=r:
            llc.append((i,j))
            break
print(llc)

#distance = math.sqrt((x - circle_x) ** 2 + (y - circle_y) ** 2)
