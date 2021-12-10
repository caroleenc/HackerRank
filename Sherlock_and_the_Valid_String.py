#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs[0]=interview-preparation-kit&playlist_slugs[1]=strings

import math
import os
import random
import re
import sys

def caroleenIsValid(s):
    letter_dict = {}
    counter_dict = {}

    if len(s) < 2:
        return "YES"

    for char in sorted(s):
        if not char in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    #print(letter_dict)

    for key in letter_dict:
        if letter_dict[key] not in counter_dict:
            counter_dict[letter_dict[key]] = 1
        else:
            counter_dict[letter_dict[key]] += 1

    #print(counter_dict[list(counter_dict)[0]])
    #print(list(counter_dict)[0])

    if len(counter_dict) > 2:
        return "NO"
    elif len(counter_dict) == 1:
        return "YES"
    elif (counter_dict[list(counter_dict)[0]] == 1 or counter_dict[list(counter_dict)[1]] == 1) and (
            list(counter_dict)[0] == list(counter_dict)[1] + 1 or list(counter_dict)[0] == list(counter_dict)[1] - 1):
        return "YES"
    elif (counter_dict[list(counter_dict)[0]] == 1 and list(counter_dict)[0] == 1) or (
            counter_dict[list(counter_dict)[1]] == 1 and list(counter_dict)[1] == 1):
        return "YES"
    else:
        return "NO"


def jeremyIsValid(string):
    string_counter = {}
    for element in string:
        if element in string_counter:
            string_counter[element] += 1
        else:
            string_counter[element] = 1

    string_optimize = list(string_counter.values())

    counter = 0
    for element in string_optimize:
        current_frequency = string_optimize.count(element)
        if current_frequency > counter:
            counter = current_frequency
            num = element

    string_optimize = [e - num for e in string_optimize]

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


def getAnswers(string):
    print('Caroleen\'s Answer:', caroleenIsValid(string))
    print('Jeremy\'s Answer:', jeremyIsValid(string))

def getTestCases(string_list, answers):
    counter = 0
    for testcase in range(len(string_list)):
        print(f"Test Case {counter + 1}")
        getAnswers(string_list[counter])
        print(f"Correct Answer: {answers[counter]}\n")
        counter += 1

if __name__ == '__main__':
    #s = 'daabbcdcd'
    #s = 'daabbcdd'
    #s = 'aabbccddeefghi'
    print('Test Case 0')
    s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    getAnswers(s)
    print('Correct Answer: YES\n')

    print('Test Case 1')
    s = 'abc'
    getAnswers(s)
    print('Correct Answer: YES\n')

    print('Test Case 2')
    s = 'abcc'
    getAnswers(s)
    print('Correct Answer: YES\n')

    print('Test Case 3')
    s = 'abccc'
    getAnswers(s)
    print('Correct Answer: NO\n')

    print('Test Case 4')
    s = 'aabbcd'
    getAnswers(s)
    print('Correct Answer: NO\n')

    print('Test Case 5')
    s = 'aabbccddeefghi'
    getAnswers(s)
    print('Correct Answer: NO\n')

    print('Test Case 6')
    s = 'abcdefghhgfedecba'
    getAnswers(s)
    print('Correct Answer: YES\n')

    print('Test Case 7')
    s = 'aabbc'
    getAnswers(s)
    print('Correct Answer: YES\n')

    #s = 'daabbcdcd'
    #s = 'daabbcdd'
    #s = 'aabbccddeefghi'

    s = ['ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfih\
chdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdeh\
igebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedech\
ahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfiha\
efefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieieg\
iffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibg\
cedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfi\
eihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfag\
fdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd', 'abc', 'abcc', 'abccc', 'aab\
bcd', 'aabbccddeefghi', 'abcdefghhgfedecba', 'aabbc', 'daabbcdcd', 'daabbcdd', 'aabbccddeefghi']

    a = ['YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO']

    getTestCases(s, a)

    print(s)