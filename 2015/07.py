
ll = open('in07.txt').read().splitlines()

kk = sorted(ll)


d = {}
for l in ll:
    op, symbol = l.split(' -> ')
    print('==', op, symbol)

    if 'AND' in op:
        l = op.split(' ')
        d[symbol] = d[l[0]] & d[l[2]]

    elif 'OR' in op:
        l = op.split(' ')
        d[symbol] = d[l[0]] | d[l[2]]
    elif 'LSHIFT' in op:
        l = op.split(' ')
        d[symbol] = d[l[0]] << int(l[2])
    elif 'RSHIFT' in op:
        l = op.split(' ')
        d[symbol] = d[l[0]] >> int(l[2])
    elif 'NOT' in op:        
        l = op.split(' ')        
        d[symbol] = d[l[1]] ^ 65535
    else:
        d[symbol] = int(op)
    
    print(d)

    
