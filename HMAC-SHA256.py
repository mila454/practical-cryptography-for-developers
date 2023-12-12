#Message authentication codes (MAC), HMAC (hash-based message authentication code)

import hashlib, hmac, binascii

mac = hmac.new(b'key', b'some msg', hashlib.sha256).digest()
print(binascii.hexlify(mac))
