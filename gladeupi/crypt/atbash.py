def atbash(text):
    res=''
    for c in text:
        if c.isalpha():
            a='A' if c.isupper() else 'a'
            res+=chr(ord(a)+25-(ord(c)-ord(a)))
        else:
            res+=c
    return res