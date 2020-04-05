def jumpinOnClouds(c):
    pointer = 0
    end = n - 1
    count = 0
    while pointer < end:
        if ((pointer + 2) <= end) and (c[pointer + 2] == 0):
            pointer += 2
            count += 1
        elif c[pointer + 1] == 0:
            pointer += 1
            count += 1

    print(count)


if __name__ == '__main__':

    n = int(input("Enter the Size of the Array: "))
    c = list(map(int, input("Enter the Elements of the Array : ").rstrip().split()))
    result = jumpinOnClouds(c)
