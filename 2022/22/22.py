ll = open('./2022/22/test.txt').read().splitlines()
#ll = open('./2022/22/input.txt').read().splitlines()

w = 0
h = len(ll[:-2])
m = []
for l in ll[:-2]:
    w = max(w, len(l))
    #print(l)
    m.append(list(l))

'''
di
   ^0
3  |
<--.-->1
   |
   v2
'''
pos = (ll[0].index('.'), 0)
di = 1
print(pos, di)

import re
path = re.split(r'([RL])',ll[-1])

def can_walk(pos,di):
    x,y = pos

    if di == 1: # looking to right

        if (x+1 < len(m[y])):
            if ('.' == m[y][x+1]):
                x+=1
        else: # out of bound
            if ('#' not in m[y] or
                m[y].index('.') < m[y].index('#')):
                x = m[y].index('.')

    elif di == 3: # looking to left
        if (x-1 >= 0):
            if ('.' == m[y][x-1]):
                x-=1
        else: # out of bound
            if ('#' not in m[y] or
                m[y].rindex('.') > m[y].rindex('#')):
                x = m[y].rindex('.')

    elif di == 2: # looking down
        if (y+1 < h):
            if ('.' == m[y+1][x]):
                y+=1
        else: # out of bound
            if (x < len(m[0])) and ('.' == m[0][x]):
                y=0
    elif di == 0: # looking up
        if (y-1 >= 0):
            if ('.' == m[y-1][x]):
                y-=1
        else: # out of bound
            if (x < len(m[h-1])) and ('.' == m[0][h-1]):
                y=h-1
    #print(pos, x,y,m[y][x])
    return (x,y)



for p in path:
    if p.isnumeric():
        mv = int(p)
        print('-',mv,'steps')
        for i in range(mv):
            new_pos = can_walk(pos,di)
            pos = new_pos

            print(i, pos, di)
    elif 'L' == p:

        print('- Left')
        di = (di-1)%4
        print(pos, di)
    elif 'R' == p:
        print('- Right')
        di = (di+1)%4
        print(pos, di)
    else:

        print('ERR',p)

