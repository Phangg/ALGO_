import sys

def divide(n, r, c, cnt):
    if n == 2:
        if r == 0 and c == 0:
            cnt += 0
        elif r == 0 and c:
            cnt += 1
        elif r and c == 0:
            cnt += 2
        else:
            cnt += 3
        return cnt
    else:
        if r < n//2 and c < n//2:                                           # 좌 상
            cnt = divide(n//2, r, c, cnt)
        elif r < n//2 and c >= n//2:                                        # 우 상
            cnt = divide(n//2, r, c-(n//2), cnt+(n//2)**2)
        elif r >= n//2 and c < n//2:                                        # 좌 하
            cnt = divide(n//2, r-(n//2), c, cnt+((n//2)**2)*2)
        elif r >= n//2 and c >= n//2:                                       # 우 하
            cnt = divide(n//2, r-(n//2), c-(n//2), cnt+(((n//2)**2)*3))     # ex) N=3 , n=8, 각 사각형의 첫값 시작 = 16*i
        return cnt

N, r, c = map(int, sys.stdin.readline().split())

ans = divide(2**N, r, c, 0)
print(ans)