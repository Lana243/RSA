import secrets
from math import log2 as log
from math import gcd

def find_two_power(x):
    s = 0
    while x % 2 == 0:
        x //= 2
        s += 1
    return s, x
            
def test_miller_rabin(n, a, s, d):   
    cur = pow(a, d, n)
    if cur == 1 or cur == n - 1:
        return 1
    for i in range(1, s):
        cur = cur ** 2 % n
        if cur == n - 1:
            return 1
    return 0
            
def strong_pseudoprime(n):
    s, d = find_two_power(n - 1)
    k = int(log(n)) + 1
    check = []
    while len(check) < k:
        a = secrets.randbelow(n - 1) + 1
        if gcd(a, n) != 1:
            return 0
        if a in check:
            continue
        check.append(a)
    for a in check:
        if not test_miller_rabin(n, a, s, d):
            return 0
    return 1
            
def try_find_prime(min_bit, max_bit):            
    bits = secrets.choice([i for i in range(min_bit, max_bit + 1)])
    n = secrets.randbits(bits)
    if (n < 2 ** (bits - 1)):
        n += 2 ** (bits - 1)
    if strong_pseudoprime(n):
        return n
    return 0

def gen_pseudoprime(min_bit, max_bit):
    n = 0
    while n == 0:
        n = try_find_prime(min_bit, max_bit)
    return n