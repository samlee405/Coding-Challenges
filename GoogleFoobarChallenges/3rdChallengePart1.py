# def answer(start, length):
#     idNumber = start
#     valueToReturn = start
#     numberOfValuesToPass = length
#
#     while numberOfValuesToPass > 0:
#         for index in range(0, numberOfValuesToPass):
#             if idNumber > 2000000000: # 2 billion
#                 print("Reached 2 billion cap, return value")
#                 return valueToReturn
#
#             if idNumber != start:
#                 valueToReturn ^= idNumber
#
#             idNumber += 1
#
#         if numberOfValuesToPass != length:
#             idNumber += (length - numberOfValuesToPass)
#
#         numberOfValuesToPass -= 1
#
#     return valueToReturn

def answer(start, length):
    currentIDValue = start
    valueToReturn = 0
    numberOfValuesToPass = length - 1

    while numberOfValuesToPass >= 0:
        currentIDValue += length - 1
        if currentIDValue % 4 == 0:
            valueToReturn ^= currentIDValue
            valueToReturn ^= cancelLowerValues(currentIDValue - numberOfValuesToPass - 1)
        elif currentIDValue % 4 == 1:
            valueToReturn ^= 1
            valueToReturn ^= cancelLowerValues(currentIDValue - numberOfValuesToPass - 1)
        elif currentIDValue % 4 == 2:
            valueToReturn ^= currentIDValue + 1
            valueToReturn ^= cancelLowerValues(currentIDValue - numberOfValuesToPass - 1)
        else:
            valueToReturn ^= 0
            valueToReturn ^= cancelLowerValues(currentIDValue - numberOfValuesToPass - 1)

        numberOfValuesToPass -= 1

    return valueToReturn

def cancelLowerValues(high):
    if high % 4 == 0:
        return (high)
    elif high % 4 == 1:
        return 1
    elif high % 4 == 2:
        return (high + 1)
    else:
        return 0

if __name__ == "__main__":
    # first case
    # print((0^1^2)^(0^1^2)^(0^1^2^3^4)^(0^1^2^3^4^5)^(0^1^2^3^4^5^6))
    # print(3^3^4^1^7)

    # second case
    # max values are 20, 16, 23, 20, 26, 24, 29, 28

    print(answer(0, 3))
    print(answer(17, 4))
