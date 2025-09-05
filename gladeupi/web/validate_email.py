import re
def validate_email(s):
    return re.match(r'^[^@]+@[^@]+\.[^@]+$',s) is not None