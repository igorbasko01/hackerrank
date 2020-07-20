# https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
    dv = (v1 - v2)
    dx = (x2 - x1)
    if dv == 0 and dx != 0:
        return 'NO'
    n_jumps = dx / dv
    return 'YES' if n_jumps >= 0 and n_jumps % 1 == 0 else 'NO'
