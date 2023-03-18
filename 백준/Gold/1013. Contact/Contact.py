import sys

# (100+1+ | 01)+
# 위 패턴을 가지는지 판별
# startswith => 문자열이 특정 문자열로 시작하는지 확인

# t: 테스트 케이스
# s: 문자열
t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()

    res = True
    while len(s) > 0:
        # 맨앞에 100 이 오면 100 제거
        if s.startswith("100"):
            s = s[3:]
            # 맨앞에 0 이 오면 0 제거
            while (len(s) > 0) and (s.startswith("0")):
                s = s[1:]

            if len(s) == 0:
                res = False
                break

            # 앞에 1이 오면 1 제거 => 조건 100 + 1 까지 만족
            s = s[1:]

            while (len(s) > 0) and (s.startswith("1")):
                # 100 일 수 도 있으니까, 보류
                if (len(s) > 3) and (s[1] == "0") and (s[2] == "0"):
                    break
                # 1 나오면 제거
                else:
                    s = s[1:]

        elif s.startswith("01"):
            s = s[2:]

        else:
            res = False
            break

    if res:
        print("YES")
    else:
        print("NO")