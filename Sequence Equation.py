arr = [1,2,3,4,5]
arr2 = [4,3,5,1,2]
i = 0
while i < len(arr):
    a = arr[i]
    if a in arr2:
        x = arr2.index(arr[i]) + 1
        if x in arr2:
            y = arr2.index(x) + 1
            print(y)
    i = i + 1
