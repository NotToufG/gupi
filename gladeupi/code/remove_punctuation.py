import re
def remove_punctuation(s):
    return re.sub(r'\W+',' ',s)