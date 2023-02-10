# Implementing LFSR in python

def setBit(value,index):
    mask = 1 << index
    return(value | mask)

def getBit(value,index):
    mask = 1 << index
    return(value & mask)

def LFSR(tap1,tap2,tap3,IV,no_bit):
    for i in range(no_bit):
        bit1 = 1 & getBit(IV,(31-tap1))
        bit2 = 1 & getBit(IV,(31-tap2))
        bit3 = getBit(IV,(31-tap3))
        IV = IV << 1
        if (bit1 ^ bit2) ^ bit3:
            IV = setBit(IV,0)
    return IV
        
bitSeq1 = 3402409650    #0b11001010110011001010011010110010
bitSeq2 = 921867418     #0b00110110111100101001010010011010
    
lfsr1 = LFSR(1,3,31,bitSeq1,10)
lfsr2 = LFSR(2,5,27,bitSeq2,10)
outputStream = lfsr1 ^ lfsr2
plaintext = 1026552546
cipher = plaintext ^ outputStream
print(cipher)


