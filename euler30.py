array=[]
fifth=[]
sum=0
for i in range(10):
	array.append(i**5)

for i in range(2,1000000):
	digits=map(int, str(i))
	numb=0
	for j in digits:
		numb+=array[j]
	if numb==i:
		fifth.append(numb)
		sum+=numb
print(fifth)
print(sum)
