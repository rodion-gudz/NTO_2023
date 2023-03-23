from math import ceil, sqrt


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)
    o = c
    # Search for an equivalence in the table. Giant step.
    for j in range(N):

        y = (h *o) % p
        o=o*c
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


import requests
import json

r = requests.get('http://10.10.21.10:1176/shared_flag')
m = json.loads(r.content)
p = m['p']
sf = m['shared_flag']


print(bsgs(2, sf, p))