import sys
from hammingDistance import findHammingDistance
from hexToB64 import load_file_as_bits

def checkKeysize(keysize, arr):
    chunk1 = "".join(arr[0:keysize])
    chunk2 = "".join(arr[keysize:keysize*2])

    return findHammingDistance(chunk1, chunk2)

def smallestHam(arr):
    smallestHams = []
    for i in range(2, 41):
        newHam = checkKeysize(i, arr)
        smallestHams.append(newHam / i)

    return smallestHams

def keysizeChunker(arr, chunksize):
    b64text = "".join(arr)
    chunked = []
    for i in range(6 * chunksize, len(b64text) + 1, 6 * chunksize):
        chunked.append(b64text[i-6*chunksize:i])
    chunkeded = []
    for chunk in chunked:
        tempChunk = []
        for i in range(6, len(chunk) + 1, 6):
            tempChunk.append(chunk[i-6:i])
        
        chunkeded.append(tempChunk)
    byteBlocks = []
    for i in range(0, chunksize):
        byteBlock = []
        for block in chunkeded:
            block[i] = (int(block[i], 2))
            byteBlock.append(block[i])
        byteBlocks.append(byteBlock)
    return byteBlocks

def XORBlock(arr):
    base64_table = {
        0: 'A',  1: 'B',  2: 'C',  3: 'D',  4: 'E',  5: 'F',  6: 'G',  7: 'H',
        8: 'I',  9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
        16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
        24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f',
        32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n',
        40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v',
        48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3',
        56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
    }
    arrayOfFreqs = []
    for i in range(0, 63): 
        freqDict = {}
        for elem in arr:
            xored = i ^ elem
            xoredStr = base64_table[int(xored)].lower()
            if xoredStr not in freqDict:
                freqDict[xoredStr] = 1
            else:
                freqDict[xoredStr] += 1
        for key in freqDict:
            freqDict[key] = freqDict[key] / len(arr)
        arrayOfFreqs.append(freqDict)
    return arrayOfFreqs

filename = sys.argv[1]

b64arr = load_file_as_bits(filename)
littleHam = smallestHam(b64arr)
probKeysize = littleHam.index(min(littleHam)) + 1
b64Chunked = keysizeChunker(b64arr, probKeysize)
print(probKeysize)
print(littleHam)
print(b64Chunked)
testThis = XORBlock(b64Chunked[0])
print(testThis)



