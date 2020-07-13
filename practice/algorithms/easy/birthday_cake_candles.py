# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthday_cake_candles(arr):
    max_candle = 0
    max_count = 0
    for c in arr:
        if c > max_candle:
            max_candle = c
            max_count = 1
        elif c == max_candle:
            max_count += 1

    return max_count


def short_solution(arr):
    return arr.count(max(arr))
