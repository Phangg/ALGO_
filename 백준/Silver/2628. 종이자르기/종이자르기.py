import sys
w, h = map(int, sys.stdin.readline().split())
L = int(sys.stdin.readline())
point_lst = []
w_lst = []
h_lst = []
for _ in range(L):
    way, point = map(int, sys.stdin.readline().split())
    if way:
        w_lst.append(point)
    else:
        h_lst.append(point)
h_lst = sorted(h_lst, reverse=True)
h_lst.append(0)
w_lst = sorted(w_lst, reverse=True)
w_lst.append(0)

h_res = []
x = h
for i in h_lst:
    h_res.append(x - i)
    x = i

w_res = []
x = w
for i in w_lst:
    w_res.append(x - i)
    x = i

print(max(h_res) * max(w_res))