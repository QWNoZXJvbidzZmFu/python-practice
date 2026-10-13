from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

# 生成密钥
p = getPrime(512)
q = getPrime(512)
n = p * q

# 欧拉函数
phi = (p - 1) * (q - 1)

# 公钥指数
e = 65537
print("公钥:")
print("e =", e)
print("n =", n)

# 私钥指数
d = inverse(e, phi)# 求 e 在模 phi 下的模逆元，也就是找 d 使得 e*d ≡ 1 mod phi(e*d，除以phi，余数等于1)
print("\n私钥:")
print("d =", d)
print("n =", n)

# 2. 明文
flag = b"RSA"
m = bytes_to_long(flag)# 转整数

# 3. 加密
c = pow(m, e, n)# c = m的e次方 mod n
print("\n密文:")
print(c)

# 4. 解密
m2 = pow(c, d, n)# m2 = c的d次方 mod n
msg = long_to_bytes(m2)# 转回字符串
print("\n解密:")
print(msg)