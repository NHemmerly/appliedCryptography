import sys

def readFile():
    byteDict = {}
    bytesTotal = 0
    with open(sys.argv[1], 'rb') as f:
        while True:
            chunk = f.read(8)
            if chunk and chunk not in byteDict:
                byteDict[chunk] = 1
            elif chunk:
                byteDict[chunk] += 1
            else: 
                break
            bytesTotal += 1
    return matchFrequencies(byteDict, bytesTotal)


def matchFrequencies(byteDict, bytesTotal):
    print(bytesTotal)
    for key in byteDict:
        byteDict[key] = byteDict[key] / bytesTotal
    print(len(byteDict))
    return byteDict

def main():
    print("Program Start")
    print(readFile())

if __name__ == "__main__":
    main()

