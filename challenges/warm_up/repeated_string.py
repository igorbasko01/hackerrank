

def repeated_string(s, n):
    num_of_as = 0
    for c in s:
        if c == 'a':
            num_of_as += 1

    str_len = len(s)
    str_in_range = n // str_len
    remainder = n % str_len

    remainder_as = 0
    for i in range(remainder):
        if s[i] == 'a':
            remainder_as += 1

    return num_of_as * str_in_range + remainder_as


def repeated_string_not_mine(s, n):
    l = len(s)
    return s.count('a') * (n // l) + s[:n % l].count('a')
