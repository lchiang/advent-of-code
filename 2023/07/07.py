from functools import cmp_to_key

ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

game = [l.split() for l in ll]



# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

def get_value_part_a(c):
    if c == 'A': return 14
    elif c == 'K': return 13
    elif c == 'Q': return 12
    elif c == 'J': return 11
    elif c == 'T': return 10
    else: return int(c)

def get_value_part_b(c):
    if c == 'A': return 14
    elif c == 'K': return 13
    elif c == 'Q': return 12
    elif c == 'J': return 1
    elif c == 'T': return 10
    else: return int(c)


def isgt(a,b):
    if a==b:
        return None
    else:
        return 1 if get_value_part_a(a) > get_value_part_a(b) else -1

def isgts(s1, s2):
    for i in range(5):
        if s1[0][i] != s2[0][i]:
            return isgt(s1[0][i], s2[0][i])




def five_of_a_kind(s):
    return True if s.count(s[0])==5 else False

def four_of_a_kind(s):
    return True if (s.count(s[0])==4 or s.count(s[1])==4) else False

def full_house(s):
    return True if (len(set(s)) == 2) else False

def three_of_a_kind(s):
    return True if (s.count(s[0])==3 or s.count(s[1])==3 or s.count(s[2])==3) else False

def two_pair(s):
    a = []
    for c in list(set(s)):
        if s.count(c)==2:
            a.append(c)
    if len(a) == 2:
        return True
    else: return False

def one_pair(s):
    return True if (len(set(s)) == 4) else False


def high_card(s):
    return True if (len(set(s)) == 5) else False




l_5ofkind = []
l_4ofkind = []
l_fullhse = []
l_3ofkind = []
l_2pair = []
l_1pair = []
l_high = []



for g in game:
    if five_of_a_kind(g[0]):
        l_5ofkind.append(g)
    elif four_of_a_kind(g[0]):
        l_4ofkind.append(g)
    elif full_house(g[0]):
        l_fullhse.append(g)
    elif three_of_a_kind(g[0]):
        l_3ofkind.append(g)
    elif two_pair(g[0]):
        l_2pair.append(g)
    elif one_pair(g[0]):
        l_1pair.append(g)
    else:
        l_high.append(g)


rank = len(game)

win = 0

for g in sorted(l_5ofkind, key=cmp_to_key(isgts),reverse=True):
    win += int(g[1]) * rank
    rank -= 1


for g in sorted(l_4ofkind, key=cmp_to_key(isgts),reverse=True):

    win += int(g[1]) * rank
    rank -= 1

for g in sorted(l_fullhse, key=cmp_to_key(isgts),reverse=True):
    win += int(g[1]) * rank
    rank -= 1

for g in sorted(l_3ofkind, key=cmp_to_key(isgts),reverse=True):
    win += int(g[1]) * rank
    rank -= 1

for g in sorted(l_2pair, key=cmp_to_key(isgts),reverse=True):
    win += int(g[1]) * rank
    rank -= 1

for g in sorted(l_1pair, key=cmp_to_key(isgts),reverse=True):
    win += int(g[1]) * rank
    rank -= 1

for g in sorted(l_high, key=cmp_to_key(isgts),reverse=True):
    win += int(g[1]) * rank
    rank -= 1

print(win)






#255958162
#255522386
#your answer is too low.