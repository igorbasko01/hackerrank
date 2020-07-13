

def diagonal_diff(arr):
    total_sum = sum([arr[i][i] - arr[i][len(arr) - 1 - i] for i in range(len(arr))])
    abs_sum = total_sum if total_sum >= 0 else -total_sum

    return abs_sum
