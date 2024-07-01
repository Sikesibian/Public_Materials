import gmpy2
from Crypto.Util.number import *

def seq(t, base, n):
    x = 2
    y = base
    i = 0
    while True:
        x, y = y, (base * y - x) % n
        i += 1
        if i == t:
            return x
def william_pm1(n, ubound):
    for v in sieve_base[ : ubound]:
        print(v)
        for i in range(1, 3000):
            v = seq(i, v, n)
            p = gmpy2.gcd(v - 2, n)
            if p != 1 and p != n:
                assert n % p == 0
                return p, n // p