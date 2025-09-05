from collections import Counter
def mode(lst):
    return Counter(lst).most_common(1)[0][0]