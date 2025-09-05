def xor_cipher(text,key):
    return ''.join(chr(ord(c)^key) for c in text)