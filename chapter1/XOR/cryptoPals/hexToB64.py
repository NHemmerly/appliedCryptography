import base64
import sys

def load_file_as_bits(file):
    with open(file, "r") as the_hex:
        new_hex = the_hex.read()
    b64 = base64.b64decode(new_hex)
    b64 = "".join(["{:08b}".format(x) for x in b64])
    b64arr = []
    for i in range(6, len(b64) + 1, 6):
        b64arr.append(b64[i-6:i])
    return b64arr

