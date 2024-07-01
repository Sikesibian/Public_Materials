#sagemath
def partial_p(p_l, p_bits = 1024, n):
    p_l_bits = p_l.nbits()
    PR.<x> = PolynomialRing(Zmod(n))
    f = 2 ^ p_l_bits * x + p_l
    f = f.monic()
    roots = f.small_roots(X = 2^(p_bits - p_l_bits), beta = 0.4) 
    if roots:
        p = gcd(2 ^ p_l_bits * int(roots[0]) + p0, n)
        return ZZ(p)
def find_p(d0, x_bits, e, n):
    x = var('x')
    for k in range(1, e + 1):
        results = solve_mod([k * x^2 + (e * d0 - k * n - k) * x + k * n == 0], 2 ^ x_bits)
        for x in results:
            pl = ZZ(x[0])
            p = partial_p(pl, x_bits, n)
            if p and p != 1:
                return p
n = # 模数
e = # 加密指数
c = # 密文
d0 = # 加密指数低位
beta = 0.5
nbits = n.nbits()
d0_bits = d0.nbits()
print(f"lower {d0_bits} bits (of {nbits} bits) is given")
p = int(find_p(d0, d0_bits, e, n))
print(f"found p: {p}")
q = n // int(p)
print(f"d = {inverse_mod(e, (p - 1) * (q - 1))}")