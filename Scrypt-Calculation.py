#Scrypt (RFC 7914) is a strong cryptographic key-derivation function (KDF)
#The Scrypt config parameters are:
#N – iterations count (affects memory and CPU usage), e.g. 16384 or 2048
#r – block size (affects memory and CPU usage), e.g. 8
#p – parallelism factor (threads to run in parallel - affects the memory, CPU usage), usually 1
#password– the input password (8-10 chars minimal length is recommended)
#salt – securely-generated random bytes (64 bits minimum, 128 bits recommended)
#derived-key-length - how many bytes to generate as output, e.g. 32 bytes (256 bits)
#The memory in Scrypt is accessed in strongly dependent order at each step, so the memory access speed is the algorithm's bottleneck. The memory required to compute Scrypt key derivation is calculated as follows:
#Memory required = 128 * N * r * p bytes

#pip install scrypt

import pyscrypt

salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
passwd = b'p@$Sw0rD~7'
key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)
print("Derived key:", key.hex())
