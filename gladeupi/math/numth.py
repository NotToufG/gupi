def numth(a):
    if 10 < a % 100 < 14:
        suffix = "th"
    else:
        last_digit = a % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"
    return f"{a}{suffix}"
