import secrets
import numpy

def eratosthenes_sieve(max_n):
    is_prime = [1] * (max_n + 1)
    primes = []
    for i in range(2, max_n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = 0
    return primes
            
def gen_mask(length, bit):
    mask = [0] * length
    mask[0] = 1;
    while mask.count(1) < bit:
        new_bit = secrets.randbelow(length)
        mask[new_bit] = 1
    return mask    
            
def gen_lucas_prime(min_bit, max_bit):
    small_primes = eratosthenes_sieve(max_bit)
    ps = []
    mask = gen_mask(len(small_primes), 5)
    min_n = 2 ** min_bit
    max_n = 2 ** max_bit
    n = 1
    for i in range(len(small_primes)):
        if mask[i]:
            n *= small_primes[i]
            ps.append(small_primes[i])
    while n < max_n:
        if n >= min_n and secrets.randbelow(2):
            break
        new_prime = secrets.choice(small_primes)
        if n * new_prime <= max_n:
            n *= new_prime
            ps.append(new_prime)
        else:
            break
    ps = numpy.unique(numpy.array(ps))
    return n + 1, ps                          

def lucas_test(n, ps, a):
    if pow(a, n - 1, n) != 1:
        return 0
    for i in ps:
        if pow(a, (n - 1) // i, n) == 1:
            return 0
    return 1

def gen_primes(min_bit, max_bit):
    n, ps = gen_lucas_prime(min_bit, max_bit)
    for i in range(2, len(bin(n)) + 1):
        if lucas_test(n, ps, i):
            return n, ps, i
    return gen_primes(min_bit, max_bit)