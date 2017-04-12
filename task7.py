#AES-шифрование в режиме ECB
from Crypto.Cipher import AES
import base64
from hashlib import md5

def aes_ecb_dec(rawCipher, rawKey):
    aes = AES.new(rawKey, AES.MODE_ECB)
    return aes.decrypt(rawCipher).decode()

old_key = "YELLOW SUBMARINE"
path = "decryptAesEcb.txt"
f = open(path, "r")
b64 = f.read().replace("\n", '')
ct = base64.b64decode(b64)
key = old_key.encode() + ct[8:16]
key = md5(key).digest()
ct = ct[16:]

if __name__ == "__main__":
    print(aes_ecb_dec(ct, key))
#print(hexstr)

