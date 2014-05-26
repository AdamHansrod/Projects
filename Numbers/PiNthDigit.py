import math

def calcPi(n): 
    pi = 0 
    for k in range(n): 
        pi += (4./(8.*k+1.) - 2./(8.*k+4.) - 1./(8.*k+5.) - 1./(8.*k+6.)) / 16.**k 
    return pi

calculatedPi = calcPi(20)
print 'Calculated value   ' + "{:2f}".format(calculatedPi)
print 'Actual value of pi ' + str(math.pi)
print 'Difference         ' + str(math.pi - calculatedPi)
