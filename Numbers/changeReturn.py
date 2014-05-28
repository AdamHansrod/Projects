def getChange(money,moneyValues):
    change = []
    for typeOfCoin in moneyValues:
        count = 0
        while(True):
            if(money - typeOfCoin < 0):
                break
            else:
                money = money - typeOfCoin
                count = count + 1
        change.append(count)
    return zip(moneyValues,change)
            
moneyValues = [100,50,25,10,5,2,1]

change = getChange(2048,moneyValues)
print change

