a,b = map(str, input().split())

aa = int(a[::-1])
bb = int(b[::-1])
if aa > bb:
    print(aa)
else: 
    print(bb)