#!/bin/python3

n, limak = tuple(map(int, input().split()))

limak_idx = limak - 1
total_caught = 0

criminals = list(map(int, input().split()))
completed = []


i = 0
while i < n:
    distance = abs(limak_idx - i)
    left_side_idx = limak_idx - distance
    right_side_idx = limak_idx + distance
    if left_side_idx == limak_idx:
        if criminals[left_side_idx] == 1:
            total_caught += 1
            completed.append(left_side_idx)
    elif left_side_idx >= 0 and right_side_idx < n and left_side_idx not in completed and right_side_idx not in completed:
        if criminals[left_side_idx] == 1 and criminals[right_side_idx] == 1:
            total_caught += 2
            completed.append(left_side_idx)
            completed.append(right_side_idx)
    elif left_side_idx >= 0 and right_side_idx >= n and left_side_idx not in completed:
        if criminals[left_side_idx] == 1:
            total_caught += 1
            completed.append(left_side_idx)
    elif left_side_idx < 0 and right_side_idx < n and right_side_idx not in completed:
        if criminals[right_side_idx] == 1:
            total_caught += 1
            completed.append(right_side_idx)
    i += 1

print(total_caught)
