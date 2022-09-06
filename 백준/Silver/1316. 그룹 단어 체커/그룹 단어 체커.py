N = int(input())

result = N
for n in range(N):
    word = input()
    for w in range(len(word)-1):
        if word[w] == word[w+1]:
            pass
        elif word[w] in word[w+1:]:
            result -= 1
            break
print(result)