from Crypto.Util.number import*
class my_RSA:
    def gen_n(BITS):
        p = getPrime(BITS)
        q = getPrime(BITS)
        n = p * q
        return n, p, q

    def encrypt(plaintext, e, n):
        m = bytes_to_long(plaintext)
        c = pow(m, e, n)
        return c

    def decrypt(p, q, e, n, c):
        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)
        m = pow(c, d, n)
        pt = long_to_bytes(m)
        return pt

plaintext=b"test_RSA"
n, p, q = my_RSA.gen_n(32)
e = 0x10001
print("public key = ", (n, e))
print("c = ", my_RSA.encrypt(plaintext, e, n))
print("Your plaintext is: ", my_RSA.decrypt(p, q, e, n, my_RSA.encrypt(plaintext, e, n)))