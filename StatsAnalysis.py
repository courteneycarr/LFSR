from LinearFeedbackShiftRegister import stream
from IPython.display import display
import pandas as pd

def monobit(seq):
    oneCount = 0
    zeroCount = 0
    for bit in seq:
        if bit == 1:
            oneCount = oneCount+1
        elif bit == 0:
            zeroCount = zeroCount+1
        else:
            print("Character present that is neither 1 or 0")
            break
    dict = {"Bit" : [1,0],"Frequency" : [oneCount,zeroCount]}
    df = pd.DataFrame(dict)
    display(df)

def longestRun(numb):
    oneMax, zeroMax, oneMaxABS, zeroMaxABS = 0
    lastBit=None
    for char in numb:
        if numb.index(char) == 0:
            lastBit = char
        else:
            if char == '1':
                oneMax = oneMax+1
                if oneMax > oneMaxABS:
                    oneMaxABS = oneMax
            if char == '0':
                zeroMax == zeroMax+1
                if zeroMax > zeroMaxABS:
                    zeroMaxABS = zeroMax
    print("MAX Run of Ones",oneMaxABS,"Max Run of Zeros",zeroMaxABS)



list =[[],[],[],[],[]] # list to store output of LSFR
#Five pairs of initialisation vectors
lfsrData = [(1204514464,1069573209),
            (3904970338,1700932284),
            (2879943089,333981540),
            (3244286911,278978611),
            (1755817739,3258225595)]
#plaintext = 2168791930

# Loops five times and each time uses a different pair of IV for the LFSR from the lfsrData list of tuples 
# When each
for j in range(5):
    s = stream(lfsrData[j],10501)
    list[j].append(s)#append the binary value to the list column
    monobit(s)

    

