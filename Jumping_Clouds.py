import math
import os
import random
import re
import sys

# Write your code here
# n = 7
# c = [0, 0, 1, 1, 1, 1, 0]

# n = 100
# c = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

n = 7
c = [0, 0, 0, 0, 0, 0, 0]

def jeremy_jumpingCloud(n, c):
    count = 0
    flag = 0
    clouds = list(range(0, n))
    temp_clouds = clouds[:]
    for index, thunder in enumerate(temp_clouds):
        if c[index] == 1:
            clouds.remove(thunder)
    print(clouds)

    if len(clouds) <= 2:
        count += 1
    else:
        for index, cloud in enumerate(clouds):
            print(index, len(clouds), cloud, count)
            if index == (len(clouds) - 2):
                if flag == 0:
                    count += 1
                break
            else:
                if flag == 1:
                    flag = 0
                    continue
                else:
                    count += 1
                    diff_current = clouds[(index + 1)] - clouds[index]
                    diff_next = clouds[(index + 2)] - clouds[(index + 1)]
                    print(diff_next, diff_current)
                    if diff_current == 1 and diff_next == 1:
                        flag = 1
        print(count)


#[0, 1, 3, 4, 6]
#[1, 2, 1, 2, 0]

#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


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

