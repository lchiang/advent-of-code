import ic
import os
import time
import multiprocessing

def printscreen(m):
    #time.sleep(0.1)
    os.system('cls')
    for y in range(len(m)):
        print(''.join(m[y]))

if __name__ == '__main__':
    f = open('input15.txt')
    d = f.readline().split(',')
    d = list(map(int, d))
    d += [0 for x in range(50000)]

    print('1')


    # initialize board
    map_size = 100
    #block_cnt, score = 0, 0
    #ball_at, paddle_at = 99, 99
    m = [['' for x in range(map_size)] for y in range(map_size)]
    x, y = map_size//2, map_size//2

    '''
    Program Input:
        movement commands are understood: north (1), south (2), west (3), and east (4). 
    Progam output
        The repair droid can reply with any of the following status codes:

        0: The repair droid hit a wall. Its position has not changed.
        1: The repair droid has moved one step in the requested direction.
        2: The repair droid has moved one step in the requested direction; 
            its new position is the location of the oxygen system.
    
    '''
    
    # init game process
    parent_conn, child_conn = multiprocessing.Pipe()
    icp = multiprocessing.Process(target=ic.intercode, args=(d, child_conn))
    icp.start()
    

    while True:
        parent_conn.send(1)
        ball_moved = False
        o = parent_conn.recv()
        if (o == 'HALT'):
            break
        else:
            print(o)			  
            printscreen(m)
    
                
    icp.join()
    
