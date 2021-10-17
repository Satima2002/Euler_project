
Sum=[]
Num=[]
s=0
Sum.append(1)
Sum.append(2)
Num.append(1)
Num.append(2)
Find=[]
while s<30:
    new=int(Sum[0])+int(Sum[1])
    Sum.append(new)
    Num.append(new)
    s+=1
    del Sum[0]
for i in Num:
    if i%2==0:
        Find.append(i)
print(Num)
print(sum(Find))