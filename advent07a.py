f = open('input07.txt')
d = f.readline().split(',')
d = list(map(int, d))

def intercode(input_val, code, i):    
    while (d[i]!=99):
        #print('instruction:', d[i])
        #print(d, i, d[i])
        opcode = d[i]%100
        param1_is_pos = (d[i]//100%10 == 0)
        param2_is_pos = (d[i]//1000%10 == 0)
        param3_is_pos = (d[i]//10000%10 == 0)

        if (opcode == 1):
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            param2 = d[d[i+2]] if param2_is_pos else d[i+2]
            val = param1 + param2
            d[d[i+3]]=val
            i += 4
            
        elif (opcode == 2):
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            param2 = d[d[i+2]] if param2_is_pos else d[i+2]
            val = param1 * param2        
            d[d[i+3]]=val
            i += 4
            
        elif (opcode == 3):        
            d[d[i+1]]=input_val.pop(0)
            #print('pop input:',d[d[i+1]])
            i += 2
            
        elif (opcode == 4):
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            #print(param1)
            return param1
            i += 2
            
        elif (opcode == 5):
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            param2 = d[d[i+2]] if param2_is_pos else d[i+2]
            i = param2 if (param1 != 0) else i+3
            
        elif (opcode == 6):
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            param2 = d[d[i+2]] if param2_is_pos else d[i+2]
            i = param2 if (param1 == 0) else i+3
            
        elif (opcode == 7):
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            param2 = d[d[i+2]] if param2_is_pos else d[i+2]        
            d[d[i+3]] = 1 if param1 < param2 else 0
            
            i += 4
        elif (opcode == 8):        
            param1 = d[d[i+1]] if param1_is_pos else d[i+1]
            param2 = d[d[i+2]] if param2_is_pos else d[i+2]        
            d[d[i+3]] = 1 if param1 == param2 else 0
            i += 4
            
        else:
            break
        #print(d)
        
    #print(d[0])



def try_seq(seq, d):
    out = intercode([seq[0],0], d.copy(), 0)
    out = intercode([seq[1],out], d.copy(), 0)
    out = intercode([seq[2],out], d.copy(), 0)
    out = intercode([seq[3],out], d.copy(), 0)
    out = intercode([seq[4],out], d.copy(), 0)
    return out

max_out = 0
import itertools
for x in itertools.permutations([0,1,2,3,4], 5):

    oo = try_seq(x, d.copy())
    if oo > max_out:
        max_out = oo
print(max_out)







    
