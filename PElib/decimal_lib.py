# decimal_lib.py

from fraction import Fraction
import primesieve as ps




def decimal_terminates(numerator: int, denominator: int):
    """Returns True if a fraction terminates.
    
    decimal_terminates(numerator: int, denominator: int) -> bool"""
    
    ## Concept: All simplified fractions whose denominators have any prime factors other than
    ##          1, 2, or 5 are non-terminating in base 10.
    
    # Auto-simplify the fraction unless it is very large
    n = Fraction(numerator,denominator).denominator
    # Check for prime factors other than 1, 2, or 5 in the denominator
    if n <= 2:
        primes = [3,7]
    if n > 2:
        primes = [3,7] + [p for p in ps.primes(10,n+1)]
        # If sqrt limit is used, the function excludes the case that n is prime
        
    # If any of the primes evenly divides n, return False (denom isn't terminating)
    if any([not n%p for p in primes]):
        return False
    return True # Return true by default




def shortest_subsequence(seq):
    # O(n^2), this should be optimized
    """Returns the shortest repeating subsequence of the given sequence. Returns [-1] if no subsequence found.
        - seq : The sequence to find a subsequence of.
        
    shortest_subsequence(seq: list) -> list"""
    
    for i in range(len(seq)):
        subseq = seq[i:]
        for j in range(1, math.ceil(len(subseq)/2)):
            verysubseq = subseq[0:j]
            if subseq == subseq[j:] + verysubseq:
                return verysubseq
    return [-1]





def reciporical_decimals(n, prec=100):
    """Gets the decimal values of the reciporical of n through long division.
    
        - n    : The number to take the reciporical of.
        - prec : The number of digits precision. (Default=100)
        
    reciporical_decimals(n: int, [prec: int]) -> list
    """
    result = []
    num = 1
    denom = n
    digits = len(str(denom))
    prec += 1
    while prec:
        if 1:
            Q = math.floor(num/denom)
            num -= Q*denom
            num *= 10**digits
            result.append(Q)
            prec -= 1
    return result[1:]