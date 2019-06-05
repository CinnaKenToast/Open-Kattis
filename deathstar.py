n = int(input())
d = []

for i in range(n):
    d.append([int(x) for x in input().split()])

for row in m:
    x = 0
    for elem in row:
        x |= elem
    print(x,end=' ')
print()