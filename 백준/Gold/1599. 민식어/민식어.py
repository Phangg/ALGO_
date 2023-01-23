import sys
from collections import defaultdict

# min : 민식어
min = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']

# 딕셔너리로 생성 (인덱스를 value 로 가지도록)
min_dict = defaultdict()
for idx, ch in enumerate(min):
    min_dict[ch] = idx
# key , value 를 반대로 갖는 딕셔너리 추가 생성
re_min_dict = {v:k for k, v in min_dict.items()}

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(sys.stdin.readline().rstrip())

# n_lst : 문자를 숫자로 변환해서 만들어줄 2차원 리스트
n_lst = []
for idx, word in enumerate(lst):
    # tmp_num : 한 단어를 숫자로 변환한 1차원 리스트
    # flag : 'ng' 를 체크할 flag
    tmp_num = []
    flag = 0
    for i, c in enumerate(word):
        if (i != (len(word)-1)) and c == 'n' and word[i+1] == 'g':
            tmp_num.append(min_dict['ng'])
            flag = 1
        elif flag:
            flag = 0
            pass
        else:
            tmp_num.append(min_dict[c])
    n_lst.append(tmp_num)

# 숫자로 변환된 2차원 배열 정렬
sort_lst = sorted(n_lst)

# 숫자를 다시 문자로 re_min_dict 을 통해 변환하면서, 형태에 맞게 출력
for num_lst in sort_lst:
    for num in num_lst:
        print(re_min_dict[num], end='')
    print()