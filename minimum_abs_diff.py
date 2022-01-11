#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def caroleen_minimumAbsoluteDifference(arr):
    minimum_bool = False
    minimum_value = 0

    arr = sorted(arr)
    print(arr)
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if minimum_bool is False:
                minimum_value = abs(arr[i]-arr[j])
                minimum_bool = True
                print(minimum_value)
            elif abs(arr[i]-arr[j]) < minimum_value:
                minimum_value = abs(arr[i]-arr[j])
                print(minimum_value)
    return print(minimum_value)

if __name__ == '__main__':
    arr1 = [-2, 4, 2]
    arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    
    result = caroleen_minimumAbsoluteDifference(arr)
