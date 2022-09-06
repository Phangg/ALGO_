N = int(input())
for _ in range(N):  
    oxlst = input()
    
    score = 0
    total = 0
    for i in oxlst:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
    
    print(total)