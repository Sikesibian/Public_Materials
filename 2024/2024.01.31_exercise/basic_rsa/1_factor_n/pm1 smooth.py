import gmpy2

def pollard_pm1(n, ubound):
    a = 2
    B = 2
    while B < ubound:
        a = pow(a, B, n)
        p = gmpy2.gcd(a - 1, n)
        if (p != 1) and (p != n):
            q = n // p
            return p, q
        B += 1