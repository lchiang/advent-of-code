import multiprocessing
import math
import ic


def param(d, i, param_num):
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, d[raw]
    # 1 = immediate mode, raw
    # 2 = relative mode, d[rel_base+raw]
    re = 0
    if (mode == 0):
        re = d[d[i+param_num]]
    elif (mode == 1):
        re = d[i+param_num]
    else: # mode = 2
        rel_pos = relative_base + d[i+param_num]
        re = d[rel_pos]
    return re
    

def param_write(d, i, param_num):    
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, raw
    # 1 = immediate mode, raw
    # 2 = relative mode, rel_base+raw
    if (mode == 0 or mode == 1):
        return d[i+param_num]
    else: # mode = 2
        return relative_base + d[i+param_num]


    
def intercode(input_val, code, i):    
    while (d[i]!=99):
        #print('instruction',i,':', d[i:i+3])
        #print(d, i, d[i])
        opcode = d[i]%100

        if (opcode == 1):
            #print(d[i:i+4], i, 1, '=', param(d,i,1), '=', param(d,i,2))
            val = param(d,i,1) + param(d,i,2)        
            d[param_write(d,i,3)]=val
            i += 4
            
        elif (opcode == 2):
            val = param(d,i,1) * param(d,i,2)        
            d[param_write(d,i,3)]=val
            i += 4
            
        elif (opcode == 3):
            d[param_write(d,i,1)]=input_val.pop(0)
            i += 2
            
        elif (opcode == 4):
            return param(d,i,1)
            i += 2
            
        elif (opcode == 5):
            i = param(d,i,2) if (param(d,i,1) != 0) else i+3
            
        elif (opcode == 6):
            i = param(d,i,2) if (param(d,i,1) == 0) else i+3
            
        elif (opcode == 7):
            d[param_write(d,i,3)] = 1 if param(d,i,1) < param(d,i,2) else 0        
            i += 4
            
        elif (opcode == 8):
            d[param_write(d,i,3)] = 1 if param(d,i,1) == param(d,i,2) else 0
            i += 4
            
        else:
            break
        #print(d)
        
    #print(d[0])


def runintercode(code, input_val):
    print("################runintercode")
    parent_conn, child_conn = multiprocessing.Pipe()
    icp = multiprocessing.Process(target=ic.intercode7, args=(code, child_conn))
    icp.start()

    while input_val:
        parent_conn.send(input_val.pop())
        
    output_val = parent_conn.recv()
    print("################", output_val)

    icp.kill()
    return output_val

def try_seq(seq, d):
    '''
    #print(111)
    out = runintercode(d.copy(), [seq[0],0])

    '''    
    out = intercode([seq[0],0], d.copy(), 0)
    out = intercode([seq[1],out], d.copy(), 0)
    out = intercode([seq[2],out], d.copy(), 0)
    out = intercode([seq[3],out], d.copy(), 0)
    out = intercode([seq[4],out], d.copy(), 0)
    return out

def part1():
    max_out = 0
    import itertools
    for x in itertools.permutations([0,1,2,3,4], 5):
        oo = try_seq(x, d.copy())
        if oo > max_out:
            max_out = oo
            print(max_out)
    print(max_out)
    
if __name__ == '__main__':
    f = open('input07a.txt')
    d = f.readline().split(',')
    d = list(map(int, d))

    #part1():

    seq = [9,8,7,6,5]

    abq = multiprocessing.Queue()
    bcq = multiprocessing.Queue()
    cdq = multiprocessing.Queue()
    deq = multiprocessing.Queue()
    eaq = multiprocessing.Queue()
    
    
    abq.put([seq[0],0])
    bcq.put(seq[1])
    cdq.put(seq[2])
    deq.put(seq[3])
    eaq.put(seq[4])

    
    icp_a = multiprocessing.Process(target=ic.intercode7, args=(d.copy(), eaq, abq))
    icp_b = multiprocessing.Process(target=ic.intercode7, args=(d.copy(), abq, bcq))
    icp_c = multiprocessing.Process(target=ic.intercode7, args=(d.copy(), bcq, cdq))
    icp_d = multiprocessing.Process(target=ic.intercode7, args=(d.copy(), cdq, deq))    
    icp_e = multiprocessing.Process(target=ic.intercode7, args=(d.copy(), deq, eaq))

    icp_a.start()
    icp_b.start()
    icp_c.start()
    icp_d.start()
    icp_e.start()

    print('a', icp_a.pid)
    print('b', icp_b.pid)
    print('c', icp_c.pid)
    print('d', icp_d.pid)
    print('e', icp_e.pid)

    #while input_val:
    #    parent_conn.send(input_val.pop())
        
    #output_val = parent_conn.recv()

    


    







    
