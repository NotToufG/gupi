def caesar_cipher(text,shift):
    res=''
    for c in text:
        if c.isalpha():
            a='A' if c.isupper() else 'a'
            res+=chr((ord(c)-ord(a)+shift)%26+ord(a))
        else:
            res+=c
    return res