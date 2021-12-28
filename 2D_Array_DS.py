def caroleen2DArray(arr):
    return "Caroleen"


def jeremy2DArray(arr):

    def getHourglassSum(ind):
        hourglass = sum([sum(arr[ind[0] - 1][(ind[1] - 1):(ind[1] + 2)]), arr[ind[0]][ind[1]], sum(arr[ind[0] + 1][(ind[1] - 1):(ind[1] + 2)])])
        return hourglass

    total = []

    for i in range(1, 5):
        for j in range(1, 5):
            total.append(getHourglassSum((i, j)))

    return max(total)

def getAnswers(string):
    print('Caroleen\'s Answer:', caroleen2DArray(string))
    print('Jeremy\'s Answer:', jeremy2DArray(string))


def getTestCases(string_list, answers):
    counter = 0
    for testcase in range(len(string_list)):
        print(f"Test Case {counter + 1}")
        getAnswers(string_list[counter])
        print(f"Correct Answer: {answers[counter]}\n")
        counter += 1


if __name__ == '__main__':

    q1 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    q2 = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
    q3 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    s = [q1, q2, q3]

    a = [7, 28, 19]

    getTestCases(s, a)
