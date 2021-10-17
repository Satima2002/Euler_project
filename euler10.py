simple=[]
for i in range(2000000):
    temp=[]
    for j in range(1,i):
        if i%j==0:
            temp.append(j)
           # j+=1
    if len(temp)<2:
        simple.append(i)
del simple[1]
del simple[0]
print(sum(simple))

# блин код правильный но интерпретатор работает медленно и поэтому почти невозможно без знания машинного обучения