scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102, 105]
pos = []
index = 0
for i in scores:
    x = alice[i]
    for j in scores:
        if scores[j] > x and scores[j+1] < x and scores[j] != scores[-1]:
            scores.insert(j+1, x)
            index = index.scores(j+1)
            pos.append(index)
        elif scores[j] > x and scores[j] == scores[-1]:
            scores.insert(j+1, x)
            index - index.scores(j+1)
            pos.append(index)
print(pos)