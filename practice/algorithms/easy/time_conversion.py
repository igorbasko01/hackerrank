# https://www.hackerrank.com/challenges/time-conversion/problem


def time_conversion(s):
    time_only = s[:-2]
    hh, mm, ss = time_only.split(':')
    ampm = s[-2:]

    if ampm == 'PM':
        h = 0 if int(hh) == 12 else int(hh)
        result = f'{h+12:02}:{mm}:{ss}'
    else:
        h = 0 if int(hh) == 12 else int(hh)
        result = f'{h:02}:{mm}:{ss}'

    return result
