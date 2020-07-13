
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def jumping_on_clouds(c):
    i = 0
    moves = 0
    while i < len(c) - 1:
        if i+2 < len(c) and c[i+2] != 1:
            i = i + 2
        else:
            i = i + 1

        moves = moves + 1

    return moves
