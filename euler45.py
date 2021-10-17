five=[]
tri=[]
six=[]
for i in range(100000):
    tri.append(i*(i+1)/2)
    five.append(i * (3 * i - 1) / 2)
    six.append(i * (2 * i - 1))

for i in tri:
    if i in five:
        if i in six:
            print(i)