c = int(input()) 

for _ in range(c):
    scores = list(map(int, input().split()))
    st_num = scores[0]
    avrg = sum(scores[1:]) / st_num

    cnt = 0 
    for score in scores[1:]:
        if score > avrg:
            cnt += 1

    new_avrg = cnt / st_num * 100


    print(f'{new_avrg:.3f}%')