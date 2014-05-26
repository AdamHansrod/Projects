def fibonacci(n):
    if n==0: return 0
    elif n==1: return 1
    else:
        fib1 = fibonacci(n-1)
        fib2 = fibonacci(n-2)
        return fib1+fib2

print 'Fibonacci number '
n = input()
print ' is ' + str(fibonacci(n))

fibList = []
for i in range(0,n):
    fibList.append(fibonacci(i))

print 'Preceeding numbers are: ' + str(fibList)
