#!/bin/python3

m1 = input()
m2 = input()
m3 = input()
measurements = [m1, m2, m3]


def the_greater(m1):
    if m1[1] == '>':
        return m1[0]
    else:
        return m1[1]

solution = {'A':0,
            'B':0,
            'C':0}
            

for i in range(len(measurements)):
    greater = the_greater(measurements[i])
    solution[greater] += 1



