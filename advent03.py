import numpy as np

f = open('input03.txt')
line1 = f.readline().split(',')
line2 = f.readline()
f.close()

#test_list = list(map(int, f.readline())) 
#print(line1[:50])
#print(line2[:60])

array_size = 20000
arr = [[0 for x in range(array_size)] for y in range(array_size)]


ind_x = 10000
ind_y = 10000

for step in line1:
    print(ind_x, ind_y)
    print(step, step[0], int(step[1:]))
    if (step[0] == 'R'):

        for x in range(int(step[1:])):
            ind_x += 1            
            arr[ind_x][ind_y] = 1
            
        print('right')
        
        
    elif (step[0] == 'L'):
        print('left')
        for x in range(int(step[1:])):
            ind_x -= 1            
            arr[ind_x][ind_y] = 1

    elif (step[0] == 'U'):
        print('up')
        for x in range(int(step[1:])):
            ind_y += 1            
            arr[ind_x][ind_y] = 1

    elif (step[0] == 'D'):
        print('down')
        for x in range(int(step[1:])):
            ind_y -= 1            
            arr[ind_x][ind_y] = 1


#for row in arr:
#    for val in row:
#        print( '{:4}'.format(val))



import numpy
a = numpy.asarray(arr)
for i in range(len(a)):    
    a[i] = a[i][::-1]    
numpy.savetxt("foo.csv", a.transpose(), fmt='%0.0f')

fromfile = open('foo.csv', 'r')
tofile = open('foo1.csv','w') 
while True:
    wline = fromfile.readline()
    if not wline:
        break
    tofile.write(wline.replace(' ','').replace('0',' '))
    
tofile.close()

print('END')


