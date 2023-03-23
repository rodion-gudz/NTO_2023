p=int(input())
sf=int(input())
k=str()

p=bin(p)[2:]
hz=[int(i) for i in p]
pp=int(len(p)*2)
a=[0]*pp
mask=2**pp
mask-=sf
mask=bin(mask)[2:]
print(mask)

for i in range(pp-1, -1, -1):
    if(mask[i]==str(a[i])):
        k+='0'
    else:
        k+='1'
        if(i-(pp//2) >=0):
            for j in range (i, i-(pp//2), -1):
                a[j]+=hz[j-(pp//2)+1]
                if(a[j] >= 2):
                    a[j-1]+=a[j]//2
                    a[j]=a[j]%2
        else:
            for j in range (i, 0, -1):
                a[j]+=hz[j-(pp//2)+1]
                if(a[j] >= 2):
                    a[j-1]+=a[j]//2
                    a[j]=a[j]%2
        print(a)
print((k))

