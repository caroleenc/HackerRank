
def getAnswers(func, string):
    print('Caroleen\'s Answer:', func(string))
    print('Jeremy\'s Answer:', func(string))

def getTestCases(string_list, answers, func):
    counter = 0
    for testcase in range(len(string_list)):
        print(f"Test Case {counter + 1}")
        getAnswers(func,string_list[counter]))
        print(f"Correct Answer: {answers[counter]}\n")
        counter += 1
    