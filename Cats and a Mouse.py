#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if x==y:
        return("Mouse C")
    elif x==z:
        return("Cat A")
    elif y==z:
        return("Cat B")
    elif (x>z and y<z) or (x<z and y>z):
        if abs(x-z)==abs(y-z):
            return("Mouse C")
        elif min(abs(x-z),abs(y-z))==abs(x-z):
            return("Cat A")
        else:
            return("Cat B")

    elif (x<z and y<z and x<y) or (x<z and y<z and x>y):
        a=max(x,y)
        if a==y:
            return("Cat B")
        else:
            return("Cat A")
    elif (x>z and y>z and y>x) or (x>z and y>z and y<x):
        b=min(x,y)
        if b==x:
            return("Cat A")
        else:
            return("Cat B")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
