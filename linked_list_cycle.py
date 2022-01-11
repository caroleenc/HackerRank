# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?isFullScreen=true&h_l=interview&playlist_slugs%\
# 5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

# Three Cases:
# Cycle to HEAD
# Cycle to MID
# NO Cycle
def caroleenHasCycle(head):
    slow = fast = head

    while (fast):
        if fast is None or fast.next is None or fast.next.next is None:
            return 0
        elif slow == fast:
            return 1
        else:
            slow = slow.next
            fast = fast.next.next


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