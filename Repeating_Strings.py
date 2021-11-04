import math

#https://www.hackerrank.com/challenges/repeated-string/submissions/code/239537677

def jeremy_repeatedstring(s, n):
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    count = count * (math.floor(n/len(s)))
    r = n % len(s)
    if r == 0:
        return count
    else:
        for i in s[:r]:
            if i == 'a':
                count += 1
        return count

def caroleen_repeatedString(s, n):
    a_count = 0
    
    string_size = len(s)
    
    for letter in s:
        if letter == 'a':
            a_count += 1
    if n % string_size == 0:
        return int(a_count * int(n/string_size))
    else:
        a_count = a_count * int(n/string_size)
        runover = n % string_size
        for letter in s[0:runover]:
            if letter == 'a':
                a_count += 1
        return int(a_count)

if __name__ == "__main__":
        
    print(jeremy_repeatedstring('aba', 10))
    # Output: 7

    print(jeremy_repeatedstring('a', 10000000))
    # Output: 10000000

    print(caroleen_repeatedString('aba', 10))
    # Output: 7

    print(caroleen_repeatedString('a', 10000000))
    # Output: 10000000
