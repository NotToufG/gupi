import re
def is_url(s):
    return re.match(r'^https?://',s) is not None