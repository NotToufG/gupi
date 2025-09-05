from collections import Counter
def most_common_word(s):
    return Counter(s.split()).most_common(1)[0][0]