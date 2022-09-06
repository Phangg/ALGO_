W = input()
W = W.upper()

ws = list(set(W))
nlst = []

for w in ws:
    nlst.append(W.count(w))

if nlst.count(max(nlst)) >= 2:
    print('?')
else:
    print(ws[nlst.index(max(nlst))])