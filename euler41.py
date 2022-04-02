def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True
for i in range(2143,12000000):	
	if(is_prime(i)):
		if (i>current):
			string=list(str(i))
			count=0
			for j in range(1,len(string)+1):
				if (str(j) in string):
					count+=1
			if (count==len(string)):
				print(i)
print(current)			
#answer : 7652413