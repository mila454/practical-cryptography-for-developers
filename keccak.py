#pip install pycryptodome

from Crypto.Hash import keccak
import binascii

keccak256 = keccak.new(data=b'hello', digest_bits=256).digest()
print("Keccak256:", binascii.hexlify(keccak256))

#Keccak256: b'1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8'
