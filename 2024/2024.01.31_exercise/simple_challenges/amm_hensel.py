from Crypto.Util.number import bytes_to_long
from secret import flag
import os

n = 3829883821474676224728554759765350402526405505378297475203016675545917027038955310987280565067907027439769858831063137150528129013866747765568167651914951885722254645384760373234321985351288857
e = 283
m = bytes_to_long(flag)

flag = flag + os.urandom(n.bit_length() // 8 - len(flag) - 1)
m = bytes_to_long(flag)

c = pow(m, e, n)

with open('out.txt', 'w') as f:
    print(f"{n = }", file=f)
    print(f"{e = }", file=f)
    print(f"{c = }", file=f)
