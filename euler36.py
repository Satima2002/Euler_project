import math
def checkIfPolindrom(numb):
		number=str(numb)
		s=0
		if(len(number)%2==0):
			for j in range(int(len(number)/2)):
				if(number[j]==number[len(number)-1-j]):
					s+=1
			if(s==(len(number)/2)):
				return True
			else:
				return False
		else:
			s+=1
			for j in range(int(len(number)/2)):
				if(number[j]==number[len(number)-1-j]):
					s+=1
			if(s==math.ceil(len(number)/2)):
				return True
			else:
				return False
sum=0
for j in range(1000000):
	y = bin(j)[2:]
	if(checkIfPolindrom(j) and checkIfPolindrom(y)):
		sum+=j
print(sum)
