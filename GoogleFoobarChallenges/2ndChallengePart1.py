def answer(l):
    unsortedArray = []

    # Separate each item in l into an array of major, minor, and revision
    for item in l:
        item = item.split(".")
        tempArray = []

        for number in item:
            tempArray.append(int(number))

        unsortedArray.append(tempArray)

    return sort(unsortedArray)

def sort(array):
    for index in range(len(array)):
        for index2 in range(index + 1, len(array)):
            if array[index2][0] < array[index][0]:
                array[index2], array[index] = array[index], array[index2]

            if array[index2][0] == array[index][0]:
                if len(array[index]) > len(array[index2]) and len(array[index2]) == 1:
                    array[index2], array[index] = array[index], array[index2]

                if len(array[index]) > 1 and len(array[index2]) > 1:
                    if array[index2][1] < array[index][1]:
                        array[index2], array[index] = array[index],  array[index2]

                    elif array[index2][1] == array[index][1]:
                        if len(array[index]) > len(array[index2]) and len(array[index2]) == 2:
                            array[index2], array[index] = array[index], array[index2]

                        if len(array[index]) > 2 and len(array[index2]) > 2:
                            if array[index2][2] < array[index][2]:
                                array[index2], array[index] = array[index], array[index2]

    return reconstructString(array)

def reconstructString(array):
    newArray = []
    for subArray in array:
        tempArray = []

        for num in subArray:
            tempArray.append(str(num))

        stringArray = ".".join(tempArray)
        newArray.append(stringArray)

    # print(newArray)
    return newArray

if __name__ == "__main__":
l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# Expected result : ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

l2 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# Expected result : ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0']

l3 = []

answer(l2)
print(['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0'])
