
iimport hashlib, time, binascii, hmac

msg = b"hello"
key = b"0"
entropy = hmac.new(key, msg, hashlib.sha256).digest()
print("Entropy:", entropy)
seed = hashlib.sha3_256(entropy).digest()
print("seed = SHA-256(entropy) =", seed)

for i in range(30):
    rand = min + bigRand % (max - min + 1)
    print(rand, " ")
