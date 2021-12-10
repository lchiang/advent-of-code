d = {} # Cost, Damage, Armor
d['Dagger']=(8,4,0)
d['Shortsword']=(10,5,0)
d['Warhammer']=(25,6,0)
d['Longsword']=(40,7,0)
d['Greataxe']=(74,8,0)

d['NoArmor']=(0,0,0)
d['Leather']=(13,0,1)
d['Chainmail']=(31,0,2)
d['Splintmail']=(53,0,3)
d['Bandedmail']=(75,0,4)
d['Platemail']=(102,0,5)

d['Damage+1']=(25,1,0)
d['Damage+2']=(50,2,0)
d['Damage+3']=(100,3,0)
d['Defense+1']=(20,0,1)
d['Defense+2']=(40,0,2)
d['Defense+3']=(80,0,3)

import itertools

weapon = ['Dagger','Shortsword','Warhammer','Longsword','Greataxe']
armor = ['NoArmor','Leather','Chainmail','Splintmail','Bandedmail','Platemail']
ring = ['Damage +1','Damage +2','Damage +3','Defense +1','Defense +2','Defense +3']

#print(list(itertools.product(a,b,c)))
print(list(itertools.combinations([0,0,1,2,3],2)))


'''
(Choose 1)
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

(Choose 0-1)
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

(Choose 0-2, No duplicate)
Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''
'''
Hit Points: 109
Damage: 8
Armor: 2

You have 100 hit points. The boss's actual stats are in your puzzle input. 
What is the least amount of gold you can spend and still win the fight?
'''

def canWin(h,d,a):
    bh, bd, ba = 12, 7, 2 #boss hit points, boss damage, boss armor
    #bh, bd, ba = 109, 8, 2 #boss hit points, boss damage, boss armor
    while h > 0 and bh > 0:
        bh -= max(1, d-ba)
        print('boss hp', bh)
        if bh <= 0:
            return True
        h -= max(1, bd-a)
        print('player hp', h)
        if h <= 0:
            return False



print('win', canWin(8,5,5))
