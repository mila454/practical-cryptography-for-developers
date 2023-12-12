#pip install argon2_cffi

import argon2, binascii

hash = argon2.hash_password_raw(
    time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32,
    password=b'password', salt=b'some salt', type=argon2.low_level.Type.ID)
print("Argon2 raw hash:", binascii.hexlify(hash))

argon2Hasher = argon2.PasswordHasher(
    time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
hash = argon2Hasher.hash("password")
print("Argon2 hash (random salt):", hash)

verifyValid = argon2Hasher.verify(hash, "password")
print("Argon2 verify (correct password):", verifyValid)

try:
    argon2Hasher.verify(hash, "wrong123")
except:
    print("Argon2 verify (incorrect password):", False)

#Argon2 raw hash: b'157f21dd3fdf7bafb76d2923ccaffa0b7be7cbae394709474d2bc66ee7b09d3e'
#Argon2 hash (random salt): $argon2id$v=19$m=32768,t=16,p=2$Rfy6J41W9idBU+n/8sZc6Q$i3QYYPtoogIAw78I2qqlUQ8vjzUXGG1V6QsBOq2NIp4
#Argon2 verify (correct password): True
#Argon2 verify (incorrect password): False
