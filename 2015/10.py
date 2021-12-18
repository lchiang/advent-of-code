s = '3113322113' # Part A Input
#s = '329356' # Part A Answer = Part B Input

from itertools import groupby
step = 0
while step < 40:
    step += 1
    q = ''
    for k, g in groupby(s):
        for c in g:
            q = q + str(sum(1 for i in g)+1) + str(k)
    s = q
    print('{:3}'.format(step), len(s))
