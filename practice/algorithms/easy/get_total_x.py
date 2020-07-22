# https://www.hackerrank.com/challenges/between-two-sets/problem


def get_total_x(a, b):
    result = 0

    for i in range(a[-1], b[0]+1):
        factors = 0
        for f in a:
            if i % f == 0:
                factors += 1

        factored = 0
        for e in b:
            if e % i == 0:
                factored += 1

        if factored == len(b) and factors == len(a):
            result += 1

    return result
