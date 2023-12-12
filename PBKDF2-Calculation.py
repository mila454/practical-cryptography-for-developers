#pip install backports.pbkdf2
#PBKDF2 is a simple cryptographic key derivation function
#PBKDF2 takes several input parameters and produces the derived key as output
#Technically, the input data for PBKDF2 consists of:
#password – array of bytes / string, e.g. "p@$Sw0rD~3" (8-10 chars minimal length is recommended)
#salt – securely-generated random bytes, e.g. "df1f2d3f4d77ac66e9c5a6c3d8f921b6" (minimum 64 bits, 128 bits is recommended)
#iterations-count, e.g. 1024 iterations
#hash-function for calculating HMAC, e.g. SHA256
#derived-key-len for the output, e.g. 32 bytes (256 bits)
#The output data is the derived key of requested length (e.g. 256 bits).

import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "p@$Sw0rD~1".encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)
print("Derived key:", binascii.hexlify(key))

#Derived key: b'52c5efa16e7022859051b1dec28bc65d9696a3005d0f97e506c42843bc3bdbc0'
