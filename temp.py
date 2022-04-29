import random
a = random.randint(2, 10)
# To find gcd of two numbers
# a is random number generated using random function.


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# exponent function


def expo(a, b):
    if(b == 0):
        return 1

    ans = a
    incr = a

    for i in range(1, b):
        for j in range(1, a):
            ans += incr
        increment = ans
    return ans

# For key generation i.e. large random number


def gen_key(q):
    key = random.randint(expo(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(expo(10, 20), q)
    return key


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x*y) % c
        y = (y*y) % c
        b = int(b/2)
    return x % c

# For asymmetric encryption


def encryption(msg, q, h, g):
    ct = []
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    print("g^k used= ", p)
    print("g^ak used= ", s)
    for i in range(0, len(ct)):
        ct[i] = s*ord(ct[i])
    return ct, p

# For decryption


def decryption(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt


msg = input("Enter message = ")
q = random.randint(expo(10, 20), expo(10, 50))
g = random.randint(2, q)
key = gen_key(q)
h = power(g, key, q)
print("q used=", q)
print("g used=", g)
print("a used=", a)
print("g^a used=", h)
ct, p = encryption(msg, q, h, g)
print("Original Message =", msg)
print("Encrypted Message =", ct)
pt = decryption(ct, p, key, q)
d_msg = ''.join(pt)
print("Decryted Message =", d_msg)
