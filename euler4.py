palind=[]
for i in range(100,1000):
    for j in range (100,1000):
        a=str(i*j)
        if len(a)==6:
            if a[0]==a[5] and a[1]==a[4] and a[2]==a[3]:
                palind.append(int(a))
print(max(palind))