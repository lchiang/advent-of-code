l = open('in16.txt').read().splitlines()[0]
#l = 'C0015000016115A2E0802F182340'

end_length = len(l) * 4

hex_as_int = int(l, 16)
hb = bin(hex_as_int)
hb = hb[2:].zfill(end_length)

total_v = 0

def read_packet(b):
    print('read:', len(b), b)
    i = 0

    version = int(b[i:i+3],2)
    i+=3
    type_id = int(b[i:i+3],2)
    i+=3
    print(i, 'version', version, 'type', type_id)

    global total_v
    total_v += version

    if type_id == 4: # literal value
        read_next = True
        lit = ''
        while read_next:
            read_next = (b[i]=='1')
            lit += b[i+1: i+5]

            i += 5
        print(i, '> literal >', int(lit,2))
    else: #operator
        length_type_id = b[i]
        i += 1
        if length_type_id == '0':
            sp_length = int(b[i:i+15],2)
            i += 15

            tl = 0
            while tl < sp_length:
                print('will read pack with length', sp_length, 'from', i+tl)
                tl += read_packet(b[i+tl:i+sp_length])
            i += sp_length
            print(i, 'done read pack')

        else: # 1
            sp_num = int(b[i:i+11],2)
            i += 11
            print('will read', sp_num, 'pack')
            for j in range(sp_num):
                leng = read_packet(b[i:])
                i += leng

    return i




read_packet(hb)

print('total version', total_v)