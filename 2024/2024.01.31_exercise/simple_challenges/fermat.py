import gmpy2
from Crypto.Util.number import *
from secret import plaintext

class my_RSA:
    def gen_n2(BITS):
        B = BITS//2
        p , q = getPrime(B) , getPrime(B)
        n = p * q * gmpy2.next_prime(p) * gmpy2.next_prime(q)
        return n
    # This is still vulnerable to fermat method!
    def encrypt(m, n, e):
        return pow(m, e, n)

# assert plaintext == b"Get_prime_is_vulnerable!" # this is a sample flag
e = 0x10001
n2 = my_RSA.gen_n2(1024)
c = my_RSA.encrypt(bytes_to_long(plaintext), n2, e)
print("(n2,e) = ", (n2, e))
print("c = ", c)
