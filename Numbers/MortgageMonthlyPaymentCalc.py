####monthly payments of morgate at X years and Y interest
def getTotalToPay(mortgage,interestRate):
    totalToPay = mortgage * interestRate
    return totalToPay

def getMonthlyPayment(totalToPay,numMonths):
    return float(totalToPay/ numMonths)

    
mortgage = input('Enter the mortgage you want: ')
interestRate = input('Enter the interest rate percentage(?.??): ')
numMonths = input('Enter the number of months you\'d like to pay it back for: ')

totalToPay = getTotalToPay(mortgage,interestRate)
monthlyPayment = getMonthlyPayment(totalToPay,numMonths)
                                     
print 'Monthly payment is: ' + str(monthlyPayment)
