import requests
import json
from math import log2

r = requests.get('http://10.10.21.10:1176/shared_flag')
m = json.loads(r.content)
p = m['p']
sf = m['shared_flag']

k=str()

p=bin(p)[2:]
hz=[int(i) for i in p]
pp=int(len(p)*2)-1
a=[0]*pp
mask=2**pp
mask-=sf
mask=bin(mask)[2:]

for i in range(pp-1, -1, -1):
    if(mask[i]==str(a[i])):
        k+='0'
    else:
        k+='1'
        if(i-(pp//2) >= 0):
            for j in range (i, i-(pp//2)-1, -1):
                a[j]+=hz[pp//2 - i+j]
                if(a[j] >= 2):
                    a[j-1]+=a[j]//2
                    a[j]=a[j]%2
    
            

p=int(p,2)
k=int((k),2)
print(log2(p*k+sf))
