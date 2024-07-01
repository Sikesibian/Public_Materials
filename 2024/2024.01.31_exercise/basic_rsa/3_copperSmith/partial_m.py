# sagemath
n = # 模数
e = # 加密指数
c = # 密文
m0 = # 明文已知位
B_bits = # 待求解x_0上界的比特位数
beta = 1 
n_bits = n.nbits()
print(f"upper {n_bits  - B_bits} bits of {n_bits} bits is given")
PR.<x> = PolynomialRing(Zmod(n))
f = (m0 + x) ^ e - c
x0 = f.small_roots(X=2^B_bits, beta=1)[0]  # 找到小于 2^B_bits 的等于 n 的因子
print("m = ", m0 + x0)