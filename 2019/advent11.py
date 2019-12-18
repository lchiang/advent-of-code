import multiprocessing
import math
import ic

def move(bot, turn):
    coor = bot[0]
    direction = bot[1]

    # move
    if direction == '^':
        print('^')
        if turn == 0: #left
            final_coor = (coor[0]-1, coor[1])
            final_dir = '<'
        else: #right
            final_coor = (coor[0]+1, coor[1])
            final_dir = '>'
    elif direction == 'v':
        print('v')
        if turn == 0: #left
            final_coor = (coor[0]+1, coor[1])
            final_dir = '>'
        else: #right
            final_coor = (coor[0]-1, coor[1])
            final_dir = '<'
    elif  direction == '>':
        print('>')
        if turn == 0: #left
            final_coor = (coor[0], coor[1]-1)
            final_dir = '^'
        else: #right
            final_coor = (coor[0], coor[1]+1)
            final_dir = 'v'
    elif direction == '<':
        print('<')
        if turn == 0: #left
            final_coor = (coor[0], coor[1]-1)
            final_dir = 'v'
        else: #right
            final_coor = (coor[0], coor[1]+1)
            final_dir = '^'

    return (final_coor, final_dir)



if __name__ == '__main__':
    f = open('input11.txt')
    d = f.readline().split(',')
    d = list(map(int, d))
    d += [0 for x in range(3501519)]

    input_val = 0
    
    parent_conn, child_conn = multiprocessing.Pipe()
    ic = multiprocessing.Process(target=ic.intercode, args=(d, input_val, child_conn))
    ic.start()

    m = []
    painted = []
    size = 5000
    for y in range(size):
        m.append([0 for x in range(size)])
        painted.append([0 for x in range(size)])

    bot = ((size//2,size//2),'^')


    def printm(m):
        s = int(math.sqrt(len(m)))
        for y in range(s):
            l = [str(m[y][x]) for x in range(s)]
            print(''.join(l))
            

    #printm(m)
    
    #   --->x
    #   |
    #   |
    #   V y
    

    parent_conn.send(0)

    
    
    col = parent_conn.recv()
    while col != 'HALT':
        turn = parent_conn.recv()
               
        
        # paint
        m[bot[0][0]][bot[0][1]] = col
        painted[bot[0][0]][bot[0][1]] += 1

        # move
        bot = move(bot, turn)
        #printm(m)

        
        parent_conn.send(m[bot[0][0]][bot[0][1]])
        
        col = parent_conn.recv()
        

    

    print('HALT')    
    ic.join()

        
        
    print(output)

