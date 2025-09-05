import hashlib
def pbkdf2(password,salt,iterations=100000):
    return hashlib.pbkdf2_hmac('sha256',password.encode(),salt.encode(),iterations)