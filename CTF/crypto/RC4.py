from Crypto.Cipher import ARC4

key = b"I_AM_REAL_KEY"      #这里填密钥，如果给的是16进制就：bytes.fromhex()

cipher = bytes.fromhex("bf2eb05478bba798256deeca2dc1734ff327f714262879d926")  #这里填密文

rc4 = ARC4.new(key)

print(rc4.decrypt(cipher))