#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    amOrPm = s[-2:]
    toReturn = ""

    if(amOrPm == "PM"):
        if(int(s[0:2]) < 12):
            toReturn = toReturn + str(12 + int(s[0:2])) + s[2:-2]
        else:
            toReturn = toReturn + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            toReturn = toReturn + "00" + s[2:-2]
        else:
            toReturn = toReturn + s[:-2]

    return toReturn

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
