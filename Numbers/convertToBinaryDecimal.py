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
    for column in reversed(columns):##get columns in the right order       
        count = 0
        while(True):
            if (decimalNumber - column < 0):
                break
            else:
                decimalNumber = decimalNumber - column 
                count = count + 1
        binaryNumber.append(count)
    return ''.join(map(str, binaryNumber)) ##return a string

def convertToDecimal(binaryString):
    binary = list(binaryString)
    columns = getListOfBinaryColumns(len(binary))##autosize the number of columns
    decimal = 0
    for column,value in zip(reversed(columns),binary):
        if (value == '1'):
            decimal += column
    return decimal
    

number = 255
binary = convertToBinary(number,8)
print binary
decimal = convertToDecimal(binary)
print decimal

print number == decimal
