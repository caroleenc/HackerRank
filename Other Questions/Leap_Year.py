# https://www.hackerrank.com/challenges/write-a-function/problem

def jeremy_is_leap(year):
    leap = False

    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

def caroleen_is_leap(year):
    leap = False

    if year % 4 == 0:
        if (year % 100 != 0 or year % 400 == 0):
            leap = True
    
    return leap

if __name__ == "__main__":
    print(jeremy_is_leap(1990))

    print(caroleen_is_leap(1990))