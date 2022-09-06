S = input()

alplst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

time = 0
for a in alplst:
    for i in a:
        for s in S:
            if s == i:
                time += alplst.index(a) + 3

print(time)