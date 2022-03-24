# import math
#
# def solution(w,h):
#     answer = 0
#     for i in range(1, w + 1):
#         h1 = math.floor((i - 1) * h / w)
#         h2 = math.ceil(i * h / w)
#         answer += (h2 - h1)
#     return (w * h) - answer

import math

def solution(w,h):
    gcd = math.gcd(w,h)
    return (w * h) - (w + h - gcd)