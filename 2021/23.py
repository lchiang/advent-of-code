
from collections import namedtuple
P = namedtuple('P', ['name','x','y'])

ll = open('in23t.txt').read().splitlines()
b = [list(l) for l in ll]
def print_board(b):
    for l in b:
        print('>',''.join(['{:2}'.format(c) for c in l]))
    print('>')
print_board(b)




def possible_route(x,y,r,rd,d):
    #print('possible_route', x, y, r)
    rr = r.copy()
    rdd = rd.copy()
    for xx, yy in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
        if b[yy][xx] == '.' and (xx,yy) not in rr: #visited
            rr.append((xx, yy))
            rdd.append((xx, yy, d+1))
            rr,rdd = possible_route(xx,yy,rr,rdd,d+1)
    return (rr,rdd)

room = {}
room['A'] = [(3,3), (3,2)]
room['B'] = [(5,3), (5,2)]
room['C'] = [(7,3), (7,2)]
room['D'] = [(9,3), (9,2)]

def possible_stop(p:P,r):
    print('possible_stop', p)
    if p.y >= 1: # in room
        # Amphipods will never stop on the space immediately outside any room.
        outside_room = [(3,1), (5,1), (7,1), (9,1)]
        return [rr for rr in r if rr not in outside_room]

    else: # if p.y == 1: # in hallway

        # Amphipods will never move from the hallway into a room unless that room
        # is their destination room and that room contains no amphipods which do
        # not also have that room as their own destination.

        # Once an amphipod stops moving in the hallway, it will stay in that spot
        # until it can move into a room.

        rm = room[p.name]
        print(rm)
        for x,y in rm:
            if b[y][x] != '.' and b[y][x] != p.name: # fill with others
                return None

        # lower room is empty
        if b[rm[0][1]][rm[0][0]] == '.':
            return [(rm[0][0],rm[0][1])] # lower room
        else:
            return [(rm[1][0],rm[1][1])] # upper room



pods = []
for y in range(len(b)):
    for x in range(len(b[y])):
        if b[y][x] in ['A','B','C','D']:
            print((b[y][x], x, y))
            (r,rd) = possible_route(x,y,[],[],0)
            print('r', r) # route
            #print(rd) # route with distance
            s = possible_stop(P(b[y][x], x, y), r)
            print('s', s)
            print()






