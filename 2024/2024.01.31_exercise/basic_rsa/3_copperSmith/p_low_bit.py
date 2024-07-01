#sagemath
n = # 模数
p_l = # 素因子低位
p_bits = 1024 # 素因子p的总位数
p_l_bits = p_l.nbits()
PR.<x> = PolynomialRing(Zmod(n))
f = 2 ^ p_l_bits * x + p_l
f = f.monic()  # 多项式首一化！十分重要的一步！！！
roots = f.small_roots(X = 2 ^ (p_bits - p_l_bits), beta = 0.4)  # 寻找小于 2^(p_bits-p_l_bits) 且大于等于 n^0.4 的因子
if roots:
    p = gcd(2 ^ p_l_bits * int(roots[0]) + p0, n)
    print(f"n = {n}\np = {p}\nq = {n//p} ")