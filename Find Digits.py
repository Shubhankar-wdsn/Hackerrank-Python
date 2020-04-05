import math
n = 1012
arr = []
num = n
j = 0
while (num != 0):
    j = num % 10
    num = math.floor(num / 10)
    arr.append(j)

count = 0
for item in arr:
    if item != 0:
        if n % item == 0:
            count = count + 1

print(count)