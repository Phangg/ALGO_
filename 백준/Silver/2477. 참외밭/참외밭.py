k = int(input())  # 1m**2 당 심을 수 있는 참외 개수

width = []  # 가로 변
height = []  # 세로 변
total = []  # 모든 변의 길이

for _ in range(6):  # 육각형으로 이루어져있다 
    d, i = map(int, input().split())  # 동서남북 방향과 거리를 6번 입력 받음
    if d == 1 or d == 2:  # 동,서 쪽
        width.append(i)
        total.append(i)
    elif d == 3 or d == 4:  # 남,북 쪽
        height.append(i)
        total.append(i)

big = max(width) * max(height)  # 가장 긴 세로 / 가로 변 을 곱해서 큰 사각형 넓이

ww = total.index(max(width))  # 가장 큰 가로 변의 인덱스
hh = total.index(max(height))  # 가장 큰 세로 변의 인덱스

no_heigt = abs(total[ww+5 if ww == 0 else ww-1] - total[ww-5 if ww == 5 else ww+1])
# 가장 긴 가로변 양 옆에 붙은 세로 변의 길이의 차 -> 빼야 할 사각형의 높이
# ww 가 0이거나 5일 경우를 넣어서 생각

no_width = abs(total[hh+5 if hh == 0 else hh-1] - total[hh-5 if hh == 5 else hh+1])
# 가장 긴 세로변 양 옆에 붙은 가로 변의 길이의 차 -> 빼야 할 사각형의 길이
# hh 가 0이거나 5일 경우를 넣어서 생각

small = no_heigt * no_width
# 빼야할 작은 사각형의 넓이

print((big - small)*k)
# 큰 사각형 - 작은 사각형 에다가 1m**2 당 심을 수 있는 참외 개수 곱하기