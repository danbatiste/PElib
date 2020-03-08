# number_lib.py

import primesieve as ps



def proper_divisors(n: int):
    """Returns the proper divisors of a number.
    
        EX: proper_divisors(12) -> [1,2,3,4,6]
        - n   : The number to find the proper divisors of.
        
    proper_divisors(n: int) -> list"""
    divisors_ = [1]
    for i in range(2,n):
        if n%i==0:
            divisors_.append(i)
    return divisors_




def divisors(n: int):
    """Returns the divisors of a number.
    
        EX: divisors(12) -> [1,2,3,4,6,12]
        - n   : The number to find the divisors of.
        
    divisors(n: int) -> list"""
    divisors_ = [1]
    for i in range(2,n):
        if n%i==0:
            divisors_.append(i)
    divisors.append(n)
    return divisors_




def prime_divisors(n: int):
    """Returns the prime divisors of a number, except 1.
    
        EX: prime_divisors(12) -> [2,3]
            prime_divisors(17) -> [17]
        - n   : The number to find the divisors of.
        
    prime_divisors(n: int) -> list"""
    divisors_ = divisors(n)[1:]
    primes_ = ps.primes(2,n+1) # Can be optimized by setting second limit to sqrt(n)
                               # I need an isprime() function first so that n can be tested
                               # for primality in a more efficient way
    pdivisors_ = [d for d in divisors_ if d in primes_] # Might be faster than searching for 
                                                        # p in divisors_
    return pdivisors_