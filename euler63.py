A=[]
for i in range(50):
    for j in range(50):
        a=i**j
        if len(str(a))==j:
            A.append(a)
print(len(A))
print(A)