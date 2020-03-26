#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    tall = 1 
    i = 0
    while i < n:
        if i % 2 != 0:
            tall = (tall + 1)
        elif i % 2 == 0:
            tall = (tall*2)
        i = i+1
    return(tall)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
