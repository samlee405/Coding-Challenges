def answer(inputValue):
    currentValue = int(inputValue)
    numberOfSteps = 0

    # print(currentValue)

    while currentValue != 1:
        if currentValue % 2 == 0:
            currentValue = currentValue / 2
        elif currentValue % 4 == 3 and currentValue != 3:
            currentValue += 1
        else:
            currentValue -= 1

        numberOfSteps += 1
        # print(currentValue)

    print(numberOfSteps)

    return numberOfSteps

import sys

# O(n) runtime, O(n) memory implementation
def min_steps_to_1(n):
    if n <= 0:
        return -1 # invalid
    if n == 1:
        return 1
    # index => number, elements => min steps
    l = [sys.maxsize for i in range(n+1)]

    # base case
    # ignore l[0] for more intutive index<=>num relationship
    l[1] = 0 # for number 1
    l[2] = 1 # for number 2

    for i in range(1,n):

        # +1, -1 operations
        n_p_1, n_m_1, n_d_2, n_mult_2 = l[i+1], l[i-1], sys.maxsize, sys.maxsize
        # get i/2 if even
        if i % 2 == 0:
            n_d_2 = l[i/2]
        # get 2i if possible
        if 2 * i <= n:
            n_mult_2 = l[2*i]

        # get the min steps among those 1 step away
        l[i] = min(min(n_p_1, n_m_1, n_d_2) + 1,l[i])

        # if the neighbors can be updated, update
        if n_p_1 > l[i] + 1:
            l[i+1] = l[i] + 1
        if n_m_1 > l[i] + 1:
            l[i-1] = l[i] + 1
        if n_mult_2 > l[i] + 1 and 2 * i <= n:
            l[2*i] = l[i] + 1
        print(l)
    return l[n]



if __name__ == '__main__':
    # answer("3465345643")
    print min_steps_to_1(4)


# exhaustive algorithms are always bad.
