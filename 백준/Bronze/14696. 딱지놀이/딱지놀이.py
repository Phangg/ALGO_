import sys

def check_figure(lst, a, b, c, d):
    star = lst.count(a)
    cir = lst.count(b)
    squ = lst.count(c)
    tri = lst.count(d)
    return [star, cir, squ, tri]

N = int(sys.stdin.readline())
for _ in range(N):
    a_lst = list(map(int, sys.stdin.readline().split()))
    b_lst = list(map(int, sys.stdin.readline().split()))
    A_figure = a_lst[1:]
    B_figure = b_lst[1:]

    ans = None                                      # ans -> 결과 값 / D: 무 , A: a 승 , B: b 승

    A_cnt = check_figure(A_figure, 4, 3, 2, 1)      # 인덱스 0:별 , 1:동그 , 2:네모 , 3:세모
    B_cnt = check_figure(B_figure, 4, 3, 2, 1)

    if A_cnt[0] > B_cnt[0]:
        ans = 'A'
    elif A_cnt[0] < B_cnt[0]:
        ans = 'B'
    else:
        if A_cnt[1] > B_cnt[1]:
            ans = 'A'
        elif A_cnt[1] < B_cnt[1]:
            ans = 'B'
        else:
            if A_cnt[2] > B_cnt[2]:
                ans = 'A'
            elif A_cnt[2] < B_cnt[2]:
                ans = 'B'
            else:
                if A_cnt[3] > B_cnt[3]:
                    ans = 'A'
                elif A_cnt[3] < B_cnt[3]:
                    ans = 'B'
                else:
                    ans = 'D'
    print(ans)