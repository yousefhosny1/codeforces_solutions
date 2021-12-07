m1 = input()
m2 = input()
m3 = input()
measurements = [m1, m2, m3]


def the_greater(m1):
    if m1[1] == '>':
        return m1[0]
    else:
        return m1[2]

def is_contridactory(dictionary):
    solutions = [0, 1, 2]
    to_be_compared = []
    for k, v in sorted(solution.items(), key = lambda p: p[1]):
        to_be_compared.append(v)
    if solutions != to_be_compared:
        return True

solution = {'A':0,
            'B':0,
            'C':0}
            

for i in range(len(measurements)):
    greater = the_greater(measurements[i])
    solution[greater] = solution.get(greater, 0) + 1

if is_contridactory(solution):
    print('Impossible')
else:
    for k, v in sorted(solution.items(), key = lambda p: p[1]):
        print(k, end='')




