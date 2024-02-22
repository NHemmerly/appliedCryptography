import sys
import math

def findHammingDistance(string1, string2):
    #string1 = openFiles(string1)
    #string2 = openFiles(string2)
    #string1 = toBinary(string1)
    #string2 = toBinary(string2)
    ham = 0
    for c in range(0, len(string1)):
        if c <= (len(string1) - 1) and c <= (len(string2) - 1):
            if string1[c] != string2[c]:
                ham += 1
    return ham

def toBinary(string):
    l,m = [],[]
    newm = []
    for i in string:
        l.append(ord(i))
    for i in l:
        m.append(str(int(bin(i)[2:])))
    for seg in m:
        seg = "0" + seg
        if len(seg) == 7:
            seg = "0" + seg
        newm.append(seg)

    return ' '.join(newm)

def openFiles(filename):
    with open(filename, 'r') as f:
        text = f.read()
        return text
