from Crypto.Util.number import long_to_bytes
def iroot3(x):
    left = 0
    right = 1 << 1024

    while left + 1 < right:
        mid = (left + right) // 2

        if mid ** 3 <= x:
            left = mid
        else:
            right = mid
    return left

c = 79253097651886336316970207450666288141474858780432928143696834386645590170887423923197063073073241450118038417504225814231878229445497010353513612779018085939487763771402062649103897914137356389
m = iroot3(c)
print(long_to_bytes(m))