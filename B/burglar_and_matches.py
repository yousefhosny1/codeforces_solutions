#!/bin/python3

matchboxes_left,  m = tuple(map(int, input().split()))

containers = []
total_matches = 0

for i in range(m):
    amount, multiplier = tuple(map(int, input().split()))
    containers.append([multiplier, amount])

containers.sort(reverse=True)

i = 0
while matchboxes_left != 0 and i < m:
    if containers[i][1] <= matchboxes_left:
        matchboxes_left -= containers[i][1]
        total_matches += containers[i][0] * containers[i][1]
    else:
        total_matches += containers[i][0] * matchboxes_left
        matchboxes_left -= matchboxes_left
    i += 1

print(total_matches)
