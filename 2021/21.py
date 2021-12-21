'''
test
Player 1 starting position: 4
Player 2 starting position: 8

real
Player 1 starting position: 6
Player 2 starting position: 1
'''


p = [4,8] # player position

#p = [5,0] # which is 6,1
m = [0,0] # marks

i = 0
pi = 0 # player 1

'''
### Part A ###
while i < 600:
    st = i*9 + 6
    p[pi] = (p[pi] - 1 + st) % 10 + 1
    m[pi] += p[pi]
    #print(i+1, 'player', pi+1, st, 'move to ', p[pi]+1, 'score', m[pi])
    if m[pi] >= 1000:
        print(pi+1, 'win')
        print('lower score * times rolled = ', min(m) * (i+1)*3)
        break
    i += 1
    pi = (pi + 1) % 2
'''

import itertools
x = [1, 2, 3]
dice = {}
for dp in itertools.product(x, repeat=3):
    if sum(dp) in dice: dice[sum(dp)] += 1
    else: dice[sum(dp)] = 1





import time
start = time.time()

w = [0,0]
def roll(st,weight, m, pi, p,r):
    pp = p.copy()
    score = m.copy()
    pp[pi] = (pp[pi] - 1 + st) % 10 + 1
    score[pi] += pp[pi]
    print('round', r, 'weight', weight, 'player', pi+1, 'st', st , p[pi],pp[pi], score[pi])
    #print('player',pi+1,', at', pp, 'score', score, 'prev', m)
    if score[pi] >= 3   : # 21
        w[pi] += weight
        #print(pi, weight, score)
    else:
        pi = (1 if pi==0 else 0)
        for k, v in dice.items():
            roll(k,v*weight,score,pi,pp,r+1)


for k, v in dice.items():
    roll(k,v,[0,0],0,p,0)



end = time.time()
print(end - start)

print(w)
