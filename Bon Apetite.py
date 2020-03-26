#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    bill_amount = 0 
    for i in range(len(bill)):
        bill_amount += bill[i]
    split = bill_amount//2
    if split == b:
        print("Bon Appetit")
    else: 
        print(b-split)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
