#!/bin/python3

import math
import os
import random
import re
import sys
def removeDuplications(num):
    num = list(dict.fromkeys(num))
    return num
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(dict.fromkeys(scores) )
    rankList = list()
    scoreLength = len(scores)
    flag = True
    position = 0
    if alice[0]>=scores[0]:
        rankList = [1 for x in alice]
    elif alice[-1]<scores[-1]:
        rankList = [scoreLength+1 for x in alice]
    else:
        for x in alice[::-1]:
            for y in range(position,scoreLength):
                if (x>=scores[y]):
                    rankList.insert(0,y+1)
                    position=y
                    flag=False
                    break
            if (flag):
                rankList.insert(0,scoreLength+1)
            flag = True
    return rankList
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
