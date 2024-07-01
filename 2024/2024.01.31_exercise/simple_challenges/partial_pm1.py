from Crypto.Util.number import *
import random
def myPrime(bits = 512):
    while True:
        n = 1
        while n.bit_length() < bits:
            n *= random.choice(sieve_base[:1000])
        if isPrime(n + 1):
            return n + 1 
def genkey(nbits = 1024):
    p, q = myPrime(nbits // 2), getPrime(nbits // 2)
    return p * q