from os import umask


print()

ll = open('in15.txt').read().splitlines()
b = [[int(x) for x in l] for l in ll]
x_max = len(b[0])-1
y_max = len(b)-1

total_risk = sum(sum(bb) for bb in b)

def print_board(bb):
    for l in bb:
        print(''.join(['{:1}'.format(c) for c in l]))
    print('-')

print_board(b)

r = {} #r[(x,y)] = risk
r[(0,0)] = 0


step = 0
while (x_max, y_max) not in r and step < 76777:
    step += 1

    connected = {}
    c = []
    for x,y in r.keys():
        if y < y_max and (x,y+1) not in r: c.append((x,y+1))
        if x < x_max and (x+1,y) not in r: c.append((x+1,y))
        if y > 0 and (x,y-1) not in r: c.append((x,y-1))
        if x > 0 and (x-1,y) not in r: c.append((x-1,y))

    c = list(set(c))
    for cx,cy in c:
        mr = total_risk
        if (cx,cy-1) in r: mr = min(mr, r[(cx,cy-1)])
        if (cx,cy+1) in r: mr = min(mr, r[(cx,cy+1)])
        if (cx-1,cy) in r: mr = min(mr, r[(cx-1,cy)])
        if (cx+1,cy) in r: mr = min(mr, r[(cx+1,cy)])
        connected[(cx,cy)] = mr + b[cy][cx]

    closest = min(connected, key=connected.get)
    r[closest] = connected[closest]

print('risk', r[(x_max, y_max)])
print(r)




print()