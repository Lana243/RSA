import secrets
from lucas import gen_primes
from miller import gen_pseudoprime

MIN_BIT = 123
MAX_BIT = 128
    
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = gcd(b % a, a)
    return g, y - b // a * x, x 
     
def get_mutually_disjoint(x):
    ans = secrets.randbelow(x)
    g, a, b = gcd(x, ans)
    if g == 1:
        return ans
    return get_mutually_disjoint(x)
                        
def gen_keys():
    p = gen_pseudoprime(MIN_BIT, MAX_BIT)
    q = gen_pseudoprime(MIN_BIT, MAX_BIT)
    n = p * q
    phi = (p - 1) * (q - 1)
    print(phi)
    e = get_mutually_disjoint(phi)
    g, d, a = gcd(e, phi)
    return n, p, q, e, (d % phi + phi) % phi

def encrypt(n, e, t):
    return pow(t, e, n)

def decrypt(n, d, s):
    return pow(s, d, n)