def getListOfBinaryColumns(numberOfBits):
    columns = []
    for column in range(0,numberOfBits):
        columns.append(2**column)
    return columns
def convertToBinary(decimalNumber,numberOfBits):
    columns = getListOfBinaryColumns(numberOfBits)
    if (sum(columns) < decimalNumber):
        return 'Not enough bits to represent decimal number ' + str(decimalNumber)
    binaryNumber = []
    for column in reversed(columns):##get out columns in the right order
        count = 0
        while(True):
            if (decimalNumber - column < 0):
                break
            else:
                decimalNumber = decimalNumber - column 
                count = count + 1
        binaryNumber.append(count)
    return ''.join(map(str, binaryNumber)) ##return a string

    

binary = convertToBinary(255,8)
print binary


