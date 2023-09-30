def getStartPoint(park):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                return (i, j) 
    
def solution(park, routes):
    answer = []
    len_x, len_y = len(park), len(park[0])
    
    now_x, now_y = getStartPoint(park)
    way_dict = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}
    
    for r in routes:
        route = r.split(" ")
        way, space = route[0], int(route[1])
        next_x, next_y = way_dict[way][0], way_dict[way][1]
        
        for i in range(1, space + 1):
            if 0 > now_x + (next_x * i) or now_x + (next_x * i) >= len_x or 0 > now_y + (next_y * i) or now_y + (next_y * i) >= len_y or park[now_x + (next_x * i)][now_y + (next_y * i)] == "X":
                break
        else:    
            now_x += (next_x * space)
            now_y += (next_y * space)
                        
    return [now_x, now_y]