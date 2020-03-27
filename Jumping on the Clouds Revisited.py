c = [1,1,1,0,1,1,0,0,0,0]
k = 3
e = 100
energy = 0
count = 0
i = 0
while True:
    if i == 0:
        count += 1
    if count < 2:
        j = 0
        if c[i] == 1:
            energy = e - 3
            e = energy
        elif c[i] == 0:
            energy = e - 1
            e = energy

        if i + k < len(c):
            i = i + k
        elif i + k >= len(c):
            j = len(c)-i
            i = k - j
    elif count == 2:
        break
print(energy)
