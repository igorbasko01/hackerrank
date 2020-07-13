# https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    for i in range(1, n+1):
        line = ''
        for x in range(n-i):
            line += ' '
        for x in range(i):
            line += '#'
        print(line)


def staircase_hacker(n):
    for i in range(n):
        print(' ' * (n - i - 1), end="")
        print('#' * (i + 1))


if __name__ == '__main__':
    staircase_hacker(3)