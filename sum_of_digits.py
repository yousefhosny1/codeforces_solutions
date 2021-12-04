#!/bin/python3

n = int(input())

counter = 0


##### RECURSION SOLUTION #########
def solution(n):
    global counter
    sumation = 0
    if n < 10:
        return counter
    while n != 0:
        sumation += n % 10
        n = int(n / 10)
    counter += 1
    return solution(sumation)


print(solution(n))

