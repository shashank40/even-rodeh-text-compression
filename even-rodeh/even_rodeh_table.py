import logging

def evenRodeh_table():
    table = {}
    
    for N in range(256):
        if N < 4:
            c = format(N, 'b')
            lc = len(c)
            codeword = '0'*(3-lc) + c
        elif N < 8:
            codeword = format(N, '03b') + '0'
        else:
            c = format(N, 'b')
            lc = len(c)
            bc = format(lc, 'b')
            codeword = bc + c + '0'
        table[N] = codeword
        
    return table

evenRodeh_table()