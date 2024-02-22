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
    return chunkeded

filename = sys.argv[1]

b64arr = load_file_as_bits(filename)
littleHam = smallestHam(b64arr)
probKeysize = littleHam.index(min(littleHam)) + 1
b64Chunked = keysizeChunker(b64arr, probKeysize)
print(probKeysize)
print(littleHam)
print(b64Chunked)



