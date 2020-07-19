# https://www.hackerrank.com/challenges/apple-and-orange/problem


def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_in = sum([1 if s <= apple + a <= t else 0 for apple in apples])
    oranges_in = sum([1 if s <= orange + b <= t else 0 for orange in oranges])

    return [apples_in, oranges_in]
