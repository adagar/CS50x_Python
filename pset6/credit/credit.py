from cs50 import get_string


def getNum():
    ccNum = get_string("Number: ")
    try:
        int(ccNum)
        return ccNum
    except ValueError:
        return getNum()


ccNum = getNum()
checkSum = 0

oddCount = 0

for i in range(len(ccNum) - 1, -1, -1):
    # print(len(ccNum) - i, end=": ")
    # print(ccNum[i], end = " ")
    if (len(ccNum) - i) % 2 == 0:
        doubledInt = int(ccNum[i]) * 2
        if(doubledInt >= 10):
            checkSum += int(str(doubledInt)[0]) + int(str(doubledInt)[1])
        else:
            checkSum += doubledInt
    else:
        int(ccNum[i])
        checkSum += int(ccNum[i])
    # print(checkSum)

amexList = [34, 37]
mastercardList = [51, 52, 53, 54, 55]
visacardList = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

# print(checkSum)

if checkSum % 10 == 0:
    firstTwo = int(ccNum[:2])
    if firstTwo in amexList:
        print("AMEX")
    elif firstTwo in mastercardList:
        print("MASTERCARD")
    elif firstTwo in visacardList:
        print("VISA")
else:
    print("INVALID")