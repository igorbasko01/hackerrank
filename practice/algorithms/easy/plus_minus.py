# https://www.hackerrank.com/challenges/plus-minus/problem
def plus_minus(arr):
    pos_ratio = 0
    neg_ratio = 0
    zero_ratio = 0
    arr_len = len(arr)
    for n in arr:
        if n > 0:
            pos_ratio += 1/arr_len
        if n < 0:
            neg_ratio += 1/arr_len
        if n == 0:
            zero_ratio += 1/arr_len

    return [round(pos_ratio, 6), round(neg_ratio, 6), round(zero_ratio, 6)]
