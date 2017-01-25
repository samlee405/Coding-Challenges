def answer(matrix):

    numerators = []
    denominators = 0

    # determine which states are terminal
    terminalStates = getTerminalStates(matrix)
    # print("The terminal states are: ")
    # print(terminalStates)

    # determine loops
    # determine various paths to terminals



def getTerminalStates(matrix):
    terminalStates = []
    index = 0
    for state in matrix:
        if all(value == 0 for value in state):
          terminalStates.append(index)

        index += 1

    return terminalStates


if __name__ == "__main__":
    testCase = [[0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

    testCase2 = [[0, 1, 0, 0, 0, 1],
                 [4, 0, 0, 3, 2, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

    answer(testCase2)
