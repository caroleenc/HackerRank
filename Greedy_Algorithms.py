# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true&h_l=interview&\
# playlist_slugs[0]=interview-preparation-kit&playlist_slugs[1]=greedy-algorithms&fbclid=IwAR2ZXOeTGwJYMbFyw4wm9J-pc6g-\
# 7vbGZljbPwr-bPEZGL95N5pTwTn8MR4

def caroleen2DArray(arr):
    return "Caroleen"


def jeremy2DArray(arr):
    arr.sort()
    subtractarr = arr[:]
    subtractarr.insert(0, 0)
    del subtractarr[-1]

    difference = []
    for arrElement, subtractarrElement in zip(arr, subtractarr):
        difference.append(arrElement - subtractarrElement)

    del difference[0]

    return min(difference)


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

    q1 = [3, -7, 0]
    q2 = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    q3 = [1, -3, 71, 68, 17]

    s = [q1, q2, q3]

    a = [3, 1, 3]

    getTestCases(s, a)
