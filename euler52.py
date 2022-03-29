
for n in range(150000):
	set1= set([int(x) for x in str(n)]) 
	set2= set([int(x) for x in str(n*2)])
	set3= set([int(x) for x in str(n*3)])
	set4= set([int(x) for x in str(n*4)])
	set5= set([int(x) for x in str(n*5)])
	set6= set([int(x) for x in str(n*6)])

	if (len(set1.difference(set2))==0 and len(set2.difference(set3))==0 and 
		len(set3.difference(set4))==0 and len(set4.difference(set5))==0 and len(set5.difference(set6))==0):
		print(n)
	
		


