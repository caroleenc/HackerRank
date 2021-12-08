#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs[0]=interview-preparation-kit&playlist_slugs[1]=strings

import math
import os
import random
import re
import sys

def caroleen_isValid(s):
    letter_dict = {}
    counter_dict = {}
    counter_array = []
    max_count = 0

    if len(s) < 2:
        return print("YES")

    for char in sorted(s):
        if not char in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char]+=1

    print(letter_dict) 

    for key in letter_dict:
        if letter_dict[key] not in counter_dict:
            counter_dict[letter_dict[key]] = 1
        else:
            counter_dict[letter_dict[key]]+= 1

    
    print(list(counter_dict)[0])
    print(list(counter_dict)[1]+1)

    if len(counter_dict) > 2:
        return "NO"
    elif len(counter_dict) == 1:
        return "YES"
    elif (counter_dict[list(counter_dict)[0]] == 1 or counter_dict[list(counter_dict)[1]] == 1) and (list(counter_dict)[0] == list(counter_dict)[1]+1 or list(counter_dict)[0] == list(counter_dict)[1]-1): 
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    #s = 'daabbcdcd'
    #s = 'daabbcdd'
    #s = 'aabbccddeefghi'
    s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    print("answer", caroleen_isValid(s))
    #caroleen_isValid2(s)