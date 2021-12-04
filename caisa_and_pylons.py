#!/bin/python3

n = int(input())
h = list(map(int, input().split()))

paid = h[0]
energy = 0

for i in range(0, len(h) - 1):
    if h[i] > h[i + 1]:
        energy += h[i] - h[i + 1]
    elif h[i] < h[i + 1]:
        energy -= h[i + 1] - h[i]
        if energy < 0:
            paid += abs(energy)
            energy = 0

print(paid)
