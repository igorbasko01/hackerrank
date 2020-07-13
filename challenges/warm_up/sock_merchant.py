import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    socks_org = {}
    pairs = 0
    for sock in ar:
        num_of_socks = socks_org.get(sock, 0)
        socks_org[sock] = num_of_socks + 1
        pairs += 1 if socks_org[sock] % 2 == 0 else 0

    return pairs
