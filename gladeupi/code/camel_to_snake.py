import re
def camel_to_snake(s):
    return re.sub('([a-z0-9])([A-Z])',r'\1_\2',s).lower()