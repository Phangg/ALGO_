from collections import defaultdict

def genre_rank(tmp_dic):
    tmp = sorted(tmp_dic.items(), key=lambda x:x[1], reverse = True)
    g_rank_lst = []
    for j in range(len(tmp)):
        g_rank_lst.append(tmp[j][0]) 
    return g_rank_lst


def top_two_in_genre(g_p_lst):
    if len(g_p_lst) > 1:
        g_p_lst = sorted(g_p_lst, key=lambda x:x[0], reverse = True)[:2]

    ans = []
    for x in g_p_lst: 
        ans.append(x[1])
    return ans
    

def solution(genres, plays):
    length = len(genres)
    
    genre_play_dict = defaultdict(list)
    genre_rank_dict = defaultdict(int)
    
    for i in range(length):
        genre_play_dict[genres[i]].append((plays[i], i))
        genre_rank_dict[genres[i]] += plays[i]
    # {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]})
    # {'classic': 1450, 'pop': 3100})
    
    first_rule = genre_rank(genre_rank_dict)
    # ['pop', 'classic']
    
    answer = []
    for genre in first_rule:
        answer += top_two_in_genre(genre_play_dict[genre])
    
    return answer