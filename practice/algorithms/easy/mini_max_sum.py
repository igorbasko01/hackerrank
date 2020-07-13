# https://www.hackerrank.com/challenges/mini-max-sum/problem
def mini_max_sum(arr):
    sortedl = sorted(arr)
    mini = sum(sortedl[0:len(arr)-1])
    maxi = sum(sortedl[1:len(arr)])

    return [mini, maxi]
