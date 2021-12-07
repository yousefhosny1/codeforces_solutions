#!/bin/python3

# O(n) Solution using Dictionary

nums = list(map(int, input().split()))
target = int(input())

dic = {}

for i, v in enumerate(nums):
    if target - v in dic:
        print([dic[target - v], i])
    else:
        dic[v] = i



