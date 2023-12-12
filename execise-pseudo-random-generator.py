# Online Python - IDE, Editor, Compiler, Interpreter

import hashlib, time, binasciib, hmac

msg = b"hello"
entropy = hmac.new(key, msg, hashlib.sha256).digest()
print("Entropy:", entropy)
startSeed = str(binascii.hexlify(hashlib.sha256(entropy.encode('ascii')).digest()))[2:-1]
print("Start seed = SHA-256(entropy) =", startSeed)

min = 10
max = 20
for i in range(5):
    nextSeed = startSeed + '|' + str(i)
    hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
    bigRand = int.from_bytes(hash, 'big')
    rand = min + bigRand % (max - min + 1)
    print(nextSeed, bigRand, '-->', rand)
