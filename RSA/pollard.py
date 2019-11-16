from math import gcd
import random
from lucas import gen_primes

N = 1000

def pollard(n):
    a = random.randrange(n)
    cur = a
    for k in range(1, N):
        cur = pow(cur, k, n)
        g = gcd(cur - 1, n)
        if g != 1 and g != n:
            return g
    return 1

