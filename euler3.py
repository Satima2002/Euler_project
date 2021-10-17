a = []
b = int(input())
for i in range(1, b + 1):
    if b % i == 0:
        a.append(i)
        i += 1
simple = []
a.reverse()
for i in a:
    temp = []
    for j in range(1, i):
        if i % j == 0:
            temp.append(j)
            j += 1
    if len(temp) < 2:
        simple.append(i)
print(simple)
