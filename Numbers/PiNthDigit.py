def pi(nthDigit, iterationsLimit):
    print 'Starting Calculation'
    step = 1.0 / iterationsLimit
    sum = 0.0
    for iteration in range(0,iterationsLimit):
        print 'Iteration ' + str(iteration)
        x = (step +0.5) * step
        sum += 4.0 / (1.0 + x * x)
    pi = step * sum
    return pi


print str(pi(3,10000))



##
##
##    
##int numSteps = 1000000000  ;
##
##          double step = 1.0 / (double) numSteps;
##
##          double sum = 0.0;
##
##          for(int i = 0 ; i < numSteps ; i++){
##              double x = (i + 0.5) * step ;
##              sum += 4.0 / (1.0 + x * x);
##          }
##
##          double pi = step * sum ;
##
##          long endTime = System.currentTimeMillis();
##
##          System.out.println("Value of pi: " + pi);
