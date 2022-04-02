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

def findFactors(x):
  
    result = []
    i = 1
    
    while i*i <= x:
        
        if (x % i == 0 ):
            result.append(i)
        
            if (x//i != i): 
                result.append(x//i)
        i += 1

    return result
for i in findFactors(600851475143):
    if(is_prime(i)):
        print(i)