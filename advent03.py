import numpy as np

f = open('input03.txt')
line1 = f.readline().split(',')
line2 = f.readline().split(',')
f.close()

def read_input_line(line):
    ind_x = 0
    ind_y = 0
    segment = []
    for step in line[:10]:
        start_x, start_y = ind_x, ind_y
        if (step[0] == 'R'):
            ind_x += int(step[1:])
            orientation = 'hori'
        elif (step[0] == 'L'):
            ind_x -= int(step[1:])
            orientation = 'hori'
        elif (step[0] == 'U'):
            ind_y += int(step[1:])
            orientation = 'vert'
        elif (step[0] == 'D'):
            ind_y -= int(step[1:])
            orientation = 'vert'
        end_x, end_y = ind_x, ind_y
        line_seg = (orientation, start_x, start_y, end_x, end_y)
        segment.append(line_seg)
        print("Step: {0}{1:4} -> {2}".format(step[0], int(step[1:]), line_seg))        
    return segment

seg1 = read_input_line(line1)

print(seg1[:10])

seg2 = read_input_line(line2)

print(seg2[:10])



#for row in arr:
#    for val in row:
#        print( '{:4}'.format(val))



# import numpy
# a = numpy.asarray(arr)
# for i in range(len(a)):    
#     a[i] = a[i][::-1]    
# numpy.savetxt("foo.csv", a.transpose(), fmt='%0.0f')
# 
# fromfile = open('foo.csv', 'r')
# tofile = open('foo1.csv','w') 
# while True:
#     wline = fromfile.readline()
#     if not wline:
#         break
#     tofile.write(wline.replace(' ','').replace('0',' '))
#     
# tofile.close()

print('END')


