import base64
def base64_encode(s):
    return base64.b64encode(s.encode()).decode()