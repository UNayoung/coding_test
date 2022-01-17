import math
from itertools import product

def solution(n):
    order = 0
    n_2 = 1
    while(True):
        if(n <= order+math.pow(3, n_2)):
            break
        order += math.pow(3, n_2)
        n_2 += 1
    permu = []
    for i in product(['1', '2', '4'], repeat=n_2):
        permu.append(''.join(i))
    return permu[int(n-order)-1]