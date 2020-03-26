#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    count = 0 
    shared = 5 
    liked = 2 
    i = 1
    while i<=n:
        count = count + liked
        shared = liked * 3
        liked = shared // 2 
        i = i+1
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
