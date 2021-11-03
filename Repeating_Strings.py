import math
import os
import random
import re
import sys


def repeatedstring(s, n):
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


repeatedstring('aba', 10)
# Output: 7

repeatedstring('a', 10000000)
# Output: 10000000
