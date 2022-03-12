n=1000000
biggest_lenght=0
biggest_number=0
tmp_biggest_number=0
for i in range(2,n):
	new_biggest_lenght=1
	tmp_biggest_number=i
	while (i!=1):
		if (i%2!=0):
			i=i*3+1
			new_biggest_lenght+=1
		else:
			i=i/2
			new_biggest_lenght+=1
	if (biggest_lenght<new_biggest_lenght):
		biggest_lenght=new_biggest_lenght
		biggest_number=tmp_biggest_number
		
print(biggest_lenght)
print(biggest_number)



			

