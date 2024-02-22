import base64
import sys

def load_file_as_bits(file):
    with open(file, "r") as the_hex:
        new_hex = the_hex.read()
    b64 = base64.b64encode(bytes.fromhex(new_hex)).decode()
    return b64

print(sys.argv[1])
b64 = load_file_as_bits(sys.argv[1])
print(b64)
