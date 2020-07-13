
def hourglass_sum(arr):
    max_sum = None
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            current_sum = 0
            current_sum += sum(arr[i][j:j+3])
            current_sum += arr[i+1][j+1]
            current_sum += sum(arr[i+2][j:j+3])

            if max_sum is None:
                max_sum = current_sum
            else:
                max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    print(hourglass_sum([[1, 1, 1, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0],
                         [0, 0, 2, 4, 4, 0],
                         [0, 0, 0, 2, 0, 0],
                         [0, 0, 1, 2, 4, 0]]))
