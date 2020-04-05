def cutTheSticks(arr):
    l = len(arr)
    while l > 0:
        if len(arr) == 0:
            break
        else:
            print(len(arr))
            x = min(arr)
            #print(x)
            n = 0
            while n < (len(arr)):
                a = arr[n]
                if a == x:
                    arr.remove(a)
                    n = n - 1
                n = n + 1

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)