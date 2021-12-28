def caroleenMinSwap2(arr):
    return "Caroleen"


def jeremyMinSwap2(arr):
    swaps = 0
    for count, element in enumerate(arr, start=1):
        if element != count:
            arr[arr.index(count)] = element
            arr[count - 1] = count
            swaps += 1

    return swaps


def getAnswers(string):
    print('Caroleen\'s Answer:', caroleenMinSwap2(string))
    print('Jeremy\'s Answer:', jeremyMinSwap2(string))


def getTestCases(questions, answers):
    counter = 0
    for testcase in range(len(questions)):
        print(f"Test Case {counter + 1}")
        getAnswers(questions[counter])
        print(f"Correct Answer: {answers[counter]}\n")
        counter += 1


if __name__ == '__main__':
    q1 = [7, 1, 3, 2, 4, 5, 6]
    q2 = [4, 3, 1, 2]
    q3 = [2, 3, 4, 1, 5]
    q4 = [1, 3, 5, 2, 4, 6, 7]

    s = [q1, q2, q3, q4]

    a = [5, 3, 3, 3]

    getTestCases(s, a)
