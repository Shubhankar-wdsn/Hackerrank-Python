#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    res = []
    for i in range(0,len(keyboards)):
        for j in range(0,len(drives)):
            res.append(keyboards[i] + drives[j])
            j = j+1
        i = i+1

    final_list = []
    for k in range(0, len(res)):
        if res[k] <= b:
            final_list.append(res[k])
            k = k+1
    if len(final_list) == 0:
        return('-1')
    else:
        return(max(final_list))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
