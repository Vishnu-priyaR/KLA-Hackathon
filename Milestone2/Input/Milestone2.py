import math
f=open("Testcase1.txt","r")
data=[]
for line in f:
    l=line.split(":")[1]
    if "x" in l:
        data.append(l.split("x")[0])
        data.append(l.split("x")[1])
    else:
        data.append(line.split(":")[1])
d,l,b,shift,r=int(data[0]),int(data[1]),int(data[2]),tuple(map(int,data[3][1:-2].split(','))),tuple(data[4])
r=d/2
llc=[]
val=int(r)
for i in range(-val,val+1,l):
    i+=shift[0]
    for j in range(-val,val+1,b):
        j+=shift[1]
        if math.sqrt((i - shift[0]) ** 2 + (j - shift[1]) ** 2) <r and (i,j) not in llc:
            llc.append((i,j))
        elif math.sqrt((i - shift[0]) ** 2 + (j+b - shift[1]) ** 2) <r and (i,j+b) not in llc:
            llc.append((i,j))
        elif math.sqrt((i+l - shift[0]) ** 2 + (j - shift[1]) ** 2) <r and (i+l,j) not in llc:
            llc.append((i,j))
        elif math.sqrt((i+l - shift[0]) ** 2 + (j+b - shift[1]) ** 2) <r and (i+l,j+b) not in llc:
            llc.append((i,j))
print(len(llc),llc)

f=open("output.txt","w")
for i in llc:
    f.write(str((i[0]//l,i[1]//b))+":"+str(i)+'\n')
f.close()
for i in llc:
    print(i[0]//l,i[1]//b,"   ",i)

