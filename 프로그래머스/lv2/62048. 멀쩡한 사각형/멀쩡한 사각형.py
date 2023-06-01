# 가로 W, 세로 H
# 8,12 -> 16 / 80 / 4
# (W * H) - (W + H - 최대공약수) 
# 최대 공약수 -> pythonic 하게 하는게 좋은디..

import math

def solution(w,h):
    total = w * h    
    return total - (w + h - math.gcd(w, h))