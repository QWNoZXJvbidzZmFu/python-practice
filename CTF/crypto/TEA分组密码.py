import struct
# ===== 修改这里：TEA密钥 =====
key = [
    0x01234567,
    0x89ABCDEF,
    0xFEDCBA98,
    0x76543210
]

# ===== 修改这里：密文 =====
cipher = bytes.fromhex(
    "68A2B669FEA39364"
    "187EEF24C76180D8"
    "59D722F11BE25ECA"
    "78938D4E0C8886C0"
)

delta = 0x9E3779B9
def tea_decrypt(v, k):
    y, z = v

    # TEA固定32轮
    sum = (delta * 32) & 0xffffffff
    for _ in range(32):
        z = (z - (
            ((y << 4) + k[2]) ^
            (y + sum) ^
            ((y >> 5) + k[3])
        )) & 0xffffffff
        y = (y - (
            ((z << 4) + k[0]) ^
            (z + sum) ^
            ((z >> 5) + k[1])
        )) & 0xffffffff
        sum = (sum - delta) & 0xffffffff
    return y, z

flag = b""


# TEA每8字节处理一次
for i in range(0, len(cipher), 8):
    block = cipher[i:i+8]

    # 大端解析(如果出现乱码，把>改为<)
    y, z = struct.unpack(">2I", block)

    y, z = tea_decrypt(
        (y, z),
        key
    )
    flag += struct.pack(">2I", y, z)

print(flag)
try:
    print(flag.decode())
except:
    pass