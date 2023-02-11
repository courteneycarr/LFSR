# Implementing LFSR in python
#Method takes integer tap values an initialization vector 
# and a desired output length as inputs. The output is the generated stream
def LFSR(tap1,tap2,tap3,tap4,IV,no_bit):
    outBit = []
    IV = IV & 0xffffffff
    for i in range(no_bit):
        #IV = IV << 1 & 0xffffffff
        # The output bit is gotten by ANDing the current state of the lfsr
        # and 1 to isolate the leftmost bit
        outBit.append((IV & (1 << 31)) >> 31)   #Append the output bit to list
        #t is the result of XORing all taps
        t = (IV >> (tap4-1)) ^ (IV >> (tap3-1)) ^ (IV >> (tap2 - 1)) ^ (IV >> (tap1 -1))
        # The XOR value is ORed with the current state of the register.
        # This acts like an if statement. A zero in the tap will produce 
        IV = (IV << 1) | (t & 1)
    return outBit

# This method takes initialisation vectors and desired length and 
# uses these to generate two 32 bit LFSRs using the LFSR method
# The output of the LFSRs are XORed to produce the key stream for the cipher
def stream(iv,l):#Takes input in the form of
    lfsr1 = LFSR(1,5,6,31,iv[0],l)
    lfsr2 = LFSR(1,2,22,32,iv[1],l)
    outputStream = []
    for i in range(l):
        outputStream.append(lfsr1[i] ^ lfsr2[i])
    return outputStream


