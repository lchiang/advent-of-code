import re
from collections import namedtuple
Pt = namedtuple('Pt', ['switch','x1','x2','y1','y2','z1','z2'])


ll = open('in22t2.txt').read().splitlines()

inp = []
for l in ll:
    match = re.search(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', l)
    il = list(match.groups())
    inp.append(Pt(*[1 if il[0] == 'on' else 0]+[int(x) for x in il[1:]]))


#   The initialization procedure only uses cubes that have x, y, and z positions of at least -50 and at most 50. For now, ignore cubes outside this region.
mi = -50
ma = 50

i = 0
d = {}

def overlapsize(p1, p2):
    x_lo = max(p1.x1, p2.x1)
    x_hi = min(p1.x2, p2.x2)

    y_lo = max(p1.y1, p2.y1)
    y_hi = min(p1.y2, p2.y2)

    z_lo = max(p1.z1, p2.z1)
    z_hi = min(p1.z2, p2.z2)

    print(x_lo, x_hi, y_lo, y_hi, z_lo, z_hi)
    return (x_hi - x_lo) * (y_hi - y_lo) * (z_hi - z_lo)


print(inp[0])
print(inp[1])

print(overlapsize(inp[0],inp[1]))



for k in inp[:2]:
    print(k)
    for z in range(k.z1,k.z2+1):
        for y in range(k.y1,k.y2+1):
            for x in range(k.x1,k.x2+1):
                d[(x,y,z)] = k.switch
                if (x,y,z) in d and k.switch == 0:
                    del d[(x,y,z)]

'''
for input line
    if +cube
        add new cube to pool
    for old cube (oc) in pool
        i_cube = new cube intersect old cube
        if oc is +
            add -i_cube to pool

        elif oc is -
            add +i_cube to pool


'''

'''
for k in inp:
    print(k)
    for z in range(max(-50,k.z1),min(51,k.z2+1)):
        for y in range(max(-50,k.y1),min(51,k.y2+1)):
            for x in range(max(-50,k.x1),min(51,k.x2+1)):
                d[(x,y,z)] = k.switch
                if (x,y,z) in d and k.switch == 0:
                    del d[(x,y,z)]
'''


print(len(d))
