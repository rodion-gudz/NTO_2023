from sympy.ntheory import discrete_log

import requests
import json

r = requests.get('http://10.10.21.10:1176/shared_flag')
m = json.loads(r.content)
p = m['p']
sf = m['shared_flag']

print(f"{p=}\n{sf=}")
print()
print()

print(discrete_log(p, sf, 2))
