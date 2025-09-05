def indent_code(s,spaces=4):
    pad=' '*spaces
    return '\n'.join(pad+line for line in s.splitlines())