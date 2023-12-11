import hashlib, binascii
sha3_256hash = hashlib.sha3_256(b'hello').digest()
print("SHA3-256('hello') =", binascii.hexlify(sha3_256hash))

#SHA3-256("hello") = "3338be694f50c5f338814986cdf0686453a888b84f424d792af4b9202398f392"
