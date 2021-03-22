#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    if (re.search("\d", password) is None):
        count+=1
    if (re.search("[A-Z]", password) is None):
        count+=1
    if (re.search("[a-z]", password) is None):
        count+=1
    if (re.search("[!@#$%^&*()-+-]", password) is None):
        count+=1
    return max(count, 6-n)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
