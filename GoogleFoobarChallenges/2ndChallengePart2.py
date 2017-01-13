def answer(l, t):
    for outerIndex in range(len(l)):
        currentSum = 0
        indexArray = []

        for innerIndex in range(outerIndex, len(l)):
            currentSum += l[innerIndex]
            indexArray.append(innerIndex)
            if currentSum == t:
                print("Found solution: ")

                return [indexArray[0], indexArray[-1]]
            elif currentSum > t:
                print("invalid")
                print(indexArray)
                break


    return [-1, -1]

if __name__ == "__main__":
    # l = [4, 3, 10, 2, 8]
    # print(answer(l, 12))

    # l = [1, 2, 3, 4]
    # print(answer(l, 15))

    # l = [4, 3, 5, 7, 8]
    # print(answer(l, 12))

    l = []
    print(answer(l, 34))
