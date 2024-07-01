#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, getPrime
from gmpy2 import invert
import os

flag = bytes_to_long(open("flag").read().encode() + os.urandom(200))

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
d = invert(e, (p - 1) * (q - 1))

encrypted_flag = pow(flag, e, n)
print(encrypted_flag)
print(n)
while True:
    c = int(input())
    print(pow(c, d, n) % 2)