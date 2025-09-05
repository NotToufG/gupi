def vigenere(text,key):
    res=''
    for i,c in enumerate(text):
        if c.isalpha():
            a='A' if c.isupper() else 'a'
            res+=chr((ord(c)-ord(a)+ord(key[i%len(key)].lower())-97)%26+ord(a))
        else:
            res+=c
    return res