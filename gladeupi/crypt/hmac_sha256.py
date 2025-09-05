import hmac,hashlib
def hmac_sha256(key,msg):
    return hmac.new(key.encode(),msg.encode(),hashlib.sha256).hexdigest()