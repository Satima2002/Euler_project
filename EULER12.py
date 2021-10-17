three=[]
i=1
j=2
three.append(i)
while i<250000:
    i+=j
    three.append(i)
    j+=1
A=[]

for i in three:
    a=[]
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
            j+=1
    if len(a)>100:
        print(i)
    A.append(len(a))
    a=[]

for i in range (500):
    i=i*(i+1)
print(i)
#print(A)
print(three)

