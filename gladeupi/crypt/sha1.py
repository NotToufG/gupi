import hashlib
def sha1(s):
    return hashlib.sha1(s.encode()).hexdigest()