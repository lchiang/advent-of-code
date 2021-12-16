ll = open('in24t.txt').read().splitlines()
ll = [int(x) for x in ll]

w = sum(ll) // 3


pp = sorted(ll, reverse=True)

print('target weight:', w)
print(pp)

g1, g2, g3 = [], [], []


def split_two(g):
    p = [x for x in pp if x not in g]
    print(g,p)


def grp(g, limit):
    if len(g) < limit:
        p = [x for x in pp if x < min(g)] if g else pp.copy()
        #print('<', g, p, sum(g) + sum(p))
        for e in p:
            ng = sum(g) + e
            np = sum(p) - e
            if ng == w:
                print('done',g+[e])
                split_two(g+[e])
            elif ng < w and ng + np >= w:
                grp(g+[e], limit)


for li in range(5):
    grp([], li)




'''

def grp(g):
    p = [x for x in pp if x < min(g)] if g else pp.copy()
    if sum(g) + sum(p) >= w:
        #print('<', g, p, sum(g) + sum(p))
        for e in p:
            ng = sum(g) + e
            if ng == w:
                print('done',g+[e])
            elif ng < w:# and ng + sum(p) > w:
                grp(g+[e])

grp([])

'''

'''

def grp(gg,ps): #[first grp], [remain packages]
    #print('>', gg,ps)
    g = gg.copy()
    rl = []
    if sum(gg) == w:
        #print('done', gg, ps)
        rl.append(gg)
    else:
        if len(ps) > 0:
            for e in ps:
                if sum(g) + e <= w and (not g or min(g)>e):
                    p = ps.copy()
                    p.remove(e)
                    rl = rl + grp(g+[e],p)
    return rl




grp1 = grp([], pp)

smallest_first_group = len(ll)
print(grp1)
print('hi')
for g in grp1:
    grp2 = grp([], [x for x in pp if x not in g])
    if len(grp2) > 0:
        print('grp2', grp2)
        smallest_first_group = min(smallest_first_group, len(g))


print(smallest_first_group)



#for p in pp:
#    print(p)
'''