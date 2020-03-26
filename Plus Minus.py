#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(arr)):
        if (arr[i]>0):
            count1 = count1 + 1
        elif (arr[i]<0):
            count2 = count2 +1
        elif(arr[i]==0):
            count3 = count3 + 1
    print(count1/len(arr))
    print(count2/len(arr))
    print(count3/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
