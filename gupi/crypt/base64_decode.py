import base64
def base64_decode(s):
    return base64.b64decode(s).decode()