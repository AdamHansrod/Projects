def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def getNextPrime(n):
    while True:
        if isprime(n)==True:
            return n
        else:
            n += 1


primes = []
while True:
    print 'Find next prime Y/N?'
    n = raw_input()
    if n == 'Y':
        ##if we have any primes then use the last known prime as a start
        if len(primes) > 0:
            print len(primes)
            lastPrime = primes[len(primes)-1]
            
            nextNumberToCheck = lastPrime + 1
            
            primes.append(getNextPrime(nextNumberToCheck))
            
            print primes
            
        else:
            primes.append(getNextPrime(1))
            
            print primes
            
    elif n == 'N':
        break
    else:
        True
print primes
