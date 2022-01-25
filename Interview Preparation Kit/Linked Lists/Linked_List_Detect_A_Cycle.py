# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?isFullScreen=true&h_l=interview&playlist_slugs%\
# 5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

def caroleenHasCycle(node):
    return node


def jeremyHasCycle(node):
    return node


def getAnswers(input):
    print('Caroleen\'s Answer:', caroleenHasCycle(input))
    print('Jeremy\'s Answer:', jeremyHasCycle(input))


def getTestCases(questions, answers):
    counter = 0
    for testcase in range(len(questions)):
        print(f"Test Case {counter + 1}")
        getAnswers(questions[counter])
        print(f"Correct Answer: {answers[counter]}\n")
        counter += 1


if __name__ == '__main__':
    q = ['Q1', 'Q2']

    a = ['A1', 'A2']

    # Run code
    getTestCases(q, a)
