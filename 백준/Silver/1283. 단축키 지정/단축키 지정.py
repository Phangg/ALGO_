import sys

N = int(sys.stdin.readline())
danchuk = []
for _ in range(N):
    word = list(map(str, sys.stdin.readline().split()))

    for i in range(len(word)):
        if word[i][0].lower() not in danchuk:
            danchuk.append(word[i][0].lower())
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            print(' '.join(word))
            break
    else:
        for j in range(len(word)):
            tmp = 0
            for k in range(1, len(word[j])):
                if word[j][k].lower() not in danchuk:
                    danchuk.append(word[j][k].lower())
                    tmp = 1
                    word[j] = word[j][:k] + '[' + word[j][k] + ']' + word[j][k+1:]
                    print(' '.join(word))
                    break
            if tmp == 1:
                break
        else:
            print(*word)