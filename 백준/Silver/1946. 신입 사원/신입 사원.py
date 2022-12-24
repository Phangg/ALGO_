import sys

# t : 테스트 케이스
t = int(sys.stdin.readline())
for _ in range(t):
    # n : 지원자 수
    n = int(sys.stdin.readline())
    # score : 지원자의 점수
    score = []
    for i in range(n):
        # p_score : 서류 점수 순위, i_score : 면접 점수 순위
        p_score, i_score = map(int, sys.stdin.readline().split())
        score.append([p_score, i_score])

    # p 기준 정렬
    score.sort()
    # p 최고 순위
    p_tmp = score[0][1]
    # 합격 인원 (정렬 상태에서 맨 앞사람은 합격이니까 1로 시작)
    ans = 1

    for j in range(1, n):
        # 지금 순위가 더 높은 사람이 있다면
        if p_tmp > score[j][1]:
            ans += 1
            p_tmp = score[j][1]

    print(ans)