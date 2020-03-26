#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high_score = [0]
    high_score.append(scores[0])
    low_score = []
    low_score.append(scores[0])
    count_high = 0
    count_low = 0
    for i in range(len(scores)):
        if (scores[i] > high_score[-1]):
            high_score.append(scores[i])
            count_high += 1
        elif (scores[i]<low_score[-1]):
            low_score.append(scores[i])
            count_low += 1
    return(count_high,count_low)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
