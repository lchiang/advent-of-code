ll = open('./2022/20/test.txt').read().splitlines()
#ll = open('./2022/20/input.txt').read().splitlines()

l = [int(x) for x in ll]


l = [1, -1, -2, 3, -5, 0, 4]
print(l)
o = l.copy()


i = 0
for x in o:
    b4_i = l.index(x)
    l.pop(b4_i)
    at_i = (b4_i + x)%(len(o)-1)

    if at_i<=0:
        at_i = len(o)-1
    l.insert(at_i, x)
    print(l, 'cycle',i,':', x, 'pos', b4_i, 'to', at_i)
    #print(l)
    i+=1

#assert([1, 2, -3, 4, 0, 3, -2]==l)


ii = l.index(0)
a = l[(ii+1000)%len(o)]
b = l[(ii+2000)%len(o)]
c = l[(ii+3000)%len(o)]
print('Part A', a,b,c)
print('Part A', a+b+c)
'''
Initial arrangement:
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2


wrong part A ans
-924
-188
'''