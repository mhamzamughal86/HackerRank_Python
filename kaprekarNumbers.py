#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    numbers = list()
    for x in range(p,q+1):
        x_length = len(str(x))

        x_square=x*x
        square_str = str(x_square)
        square_len = len(square_str)


        left_str =  square_str[:square_len-x_length:]
        left_str = "0" if left_str=='' else left_str
        right_str = square_str[square_len-x_length::]
        if(int(left_str)+int(right_str)==x):
            numbers.append(x)
    if (len(numbers)==0):
            print("INVALID RANGE")
    else:
        for x in numbers:
            print(x,end=" ")
        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
