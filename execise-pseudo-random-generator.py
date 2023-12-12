import hashlib, time, binascii, hmac

msg = b"hello"
key = b"0"
entropy = hmac.new(key, msg, hashlib.sha256).digest()
print("Entropy:", entropy)
seed = hashlib.sha3_256(entropy).digest()
print("seed = ", seed)

for i in range(30):
    rand = 1 + (int.from_bytes(entropy, byteorder = "big") - int.from_bytes(hmac.new(i.to_bytes(8, byteorder = "big", signed=True), seed, hashlib.sha256).digest(), byteorder = "big")) % 10
    print(rand, " ")
    
