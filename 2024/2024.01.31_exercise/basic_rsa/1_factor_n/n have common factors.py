from Crypto.Util.number import *
from math import *

p, q, r = getPrime(512), getPrime(512), getPrime(512)
n1 = p * q
n2 = p * r

print(n1, n2)
# use n1 and n2 to get p, q, r