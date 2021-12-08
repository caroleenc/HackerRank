#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

def caroleen_jumpingOnClouds(c,current,count):
    print("C[%s] = %s, Count: %s" % (current, c[current], count))
    if len(c) <= 1:
        return len(c)
    elif current == len(c)-1:
        return count
    elif current+2 < len(c) and c[current+2] == 0:
        return caroleen_jumpingOnClouds(c,current+2,count+1)
    elif current+1 < len(c) and c[current+1] == 0:
        return caroleen_jumpingOnClouds(c,current+1,count+1)
    
if __name__ == '__main__':
    #c = [0,0,1,0,0,1,0]
    #c = [0,0,0,1,0,0]
    c = [0,0]
    print(caroleen_jumpingOnClouds(c,0,0))
    