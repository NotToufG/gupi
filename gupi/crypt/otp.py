import secrets
def otp(length):
    return ''.join(str(secrets.randbelow(10)) for _ in range(length))