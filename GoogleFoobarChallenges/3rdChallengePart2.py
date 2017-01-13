def answer(inputValue):
    currentValue = int(inputValue)
    numberOfSteps = 0

    print(currentValue)

    while currentValue != 1:
        if currentValue % 2 == 0:
            currentValue = currentValue / 2
        elif currentValue % 4 == 3 and currentValue != 3:
            currentValue += 1
        else:
            currentValue -= 1

        numberOfSteps += 1
        print(currentValue)

    return numberOfSteps

if __name__ == '__main__':
    answer("11")


# exhaustive algorithms are always bad.
