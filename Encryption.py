import math
import os
import random
import re
import sys

s = (input().strip())
s = s.replace(" ","")
length = math.sqrt(len(s))
row = math.floor(length)
col = math.ceil(length)
rem = len(s) % col
str = " "
if rem != 0:
    str = (col - rem)*str
    s = s + str
table = ([s[i:i+col] for i in range(0, len(s), col)])
i = 0
j = 0
arr = []
for j in range(col):
    x = ''
    for i in range(len(table)):
        x = x + table[i][j]
    arr.append(x)
print(arr)
str1 = ' '
s = str1.join(arr)
print(s)
