def isValid(string):
    string_counter = {}
    for element in string:
        if element in string_counter:
            string_counter[element] += 1
        else:
            string_counter[element] = 1
    string_optimize = list(string_counter.values())
    string_optimize = [num - min(string_optimize) for num in string_optimize]

    counter = 0
    evaluate_list = []
    for check in string_optimize:
        if check == 0:
            counter += 1
        else:
            evaluate_list.append(check)

    if len(string_optimize) - counter > 1:
        return 'NO'
    else:
        if sum(evaluate_list) <= 1:
            return 'YES'
        else:
            return 'NO'


print('Test Case 1')
s = 'abc'
print(isValid(s))
print('Answer: YES\n')

print('Test Case 2')
s = 'abcc'
print(isValid(s))
print('Answer: YES\n')

print('Test Case 3')
s = 'abccc'
print(isValid(s))
print('Answer: NO\n')

print('Test Case 4')
s = 'aabbcd'
print(isValid(s))
print('Answer: NO\n')

print('Test Case 5')
s = 'aabbccddeefghi'
print(isValid(s))
print('Answer: NO\n')

print('Test Case 6')
s = 'abcdefghhgfedecba'
print(isValid(s))
print('Answer: YES\n')

print('Test Case 7')
s = 'aabbc'
print(isValid(s))
print('Answer: YES')