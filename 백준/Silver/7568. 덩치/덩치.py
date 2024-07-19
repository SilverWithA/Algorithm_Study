import sys

n = int(sys.stdin.readline())
people = []

for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    people.append([w, h])
ranks = ''
for p in people:
    ranking = 1
    # print("p= ", p)
    # print(ranking)
    w1, h1 = p
    for i in range(len(people)):

        # print(f"people[{i}]= ", people[i])
        w2, h2 = people[i]
        if w1 < w2 and h1 < h2:
            ranking += 1

    ranks += (str(ranking)+' ')
print(ranks[:-1])