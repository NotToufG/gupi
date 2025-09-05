import secrets
def random_key(n):
    return secrets.token_hex(n)