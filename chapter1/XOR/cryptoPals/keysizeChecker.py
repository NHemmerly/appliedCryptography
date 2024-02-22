import sys
from hammingDistance import findHammingDistance
from hexToB64 import load_file_as_bits

def checkKeysize(keysize, arr):
    chunk1 = "".join(arr[0:keysize])
    chunk2 = "".join(arr[keysize:keysize*2])
    print(chunk1)
    print(chunk2)


    return findHammingDistance(chunk1, chunk2)

def smallestHam(arr):
    smallestHams = []
    for i in range(2, 41):
        newHam = checkKeysize(i, arr)
        smallestHams.append(newHam / i)

    return smallestHams

filename = sys.argv[1]
keysize = sys.argv[2]


b64arr = load_file_as_bits(filename)
ham = checkKeysize(int(keysize), b64arr)
normalizedHam = ham / int(keysize)
print(ham)
print(normalizedHam)
littleHam = smallestHam(b64arr)
print(littleHam.index(min(littleHam)) + 1)
print(littleHam)



