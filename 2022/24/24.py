ll = open('./2022/24/test1.txt').read().splitlines()
#ll = open('./2022/24/input.txt').read().splitlines()

def add_to_dict(x,y,symbol,dict):
    if (x,y) not in dict:
        dict[(x,y)] = [symbol]
    else:
        dict[(x,y)].append(symbol)

w = len(ll[0])
h = len(ll)
blizzard = {}
for y in range(len(ll)):
    for x in range(len(ll[0])):
        if ll[y][x] in ['>','v','^','<']:
            add_to_dict(x,y,ll[y][x],blizzard)


print(blizzard)

def print_map(blizzard):
    for y in range(h):
        line = []
        for x in range(w):
            if (x,y) in blizzard.keys():
                v = blizzard[(x,y)]
                line.append(str(len(v)) if len(v)>1 else v[0])
            elif (x,y)==(1,0) or (x,y)==(w-2,h-1):
                line.append('.')
            elif x==0 or x==w-1 or y==0 or y==h-1:
                line.append('#')
            else:
                line.append('.')

        print(''.join(line))
    print()

print_map(blizzard)



def move(blizzard, step):
    b = {}
    for k,vv in blizzard.items():
        x0,y0 = k
        for v in vv:
            if v=='>':
                x = (x0+step-1)%(w-2)+1
                add_to_dict(x,y0,'>',b)
            elif v=='<':
                x = (x0-step-1)%(w-2)+1
                add_to_dict(x,y0,'<',b)
            elif v=='v':

                y = (y0+step-1)%(h-2)+1
                add_to_dict(x0,y,'v',b)
            elif v=='^':
                y = (y0-step-1)%(h-2)+1
                add_to_dict(x0,y,'^',b)
            else:
                print('ERR: Unknown symbol',v)





    return b

b1 = move(blizzard,1)
print_map(b1)
b1 = move(blizzard,2)
print_map(b1)
b1 = move(blizzard,3)
print_map(b1)
b1 = move(blizzard,4)
print_map(b1)