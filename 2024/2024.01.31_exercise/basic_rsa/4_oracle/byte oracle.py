from Crypto.Util.number import bytes_to_long, getPrime
from gmpy2 import invert
import os
from random import SystemRandom

rnd = SystemRandom()

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
d = invert(e, (p - 1) * (q - 1))
m = rnd.randrange(n)
c = pow(m, e, n)
print(c)
print(n)

for _ in range(300):
    c = int(input())
    print(pow(c, d, n) % 256)

guess_m = int(input())
if guess_m == m:
    print(open("flag").read())
else:
    print("Nope")