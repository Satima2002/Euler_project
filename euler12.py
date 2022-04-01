array=[]
def triangle(number):
	result=0
	for i in range(number+1):
		result+=i

	return result

def findFactors(x):
  
    result = []
    i = 1
    
    while i*i <= x:
        
        if x % i == 0:
            result.append(i)
        
            if x//i != i: 
                result.append(x//i)
        i += 1

    return result
    
for i in range(1,50000):
	factors=len(findFactors(triangle(i)))
	if(factors>=500):
		print(triangle(i))
		print(factors)
		break

