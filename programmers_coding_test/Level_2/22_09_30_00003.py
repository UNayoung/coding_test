from typing import List

def fire_power(graph, v, rang, n):
    left_up = [v[0]-1-rang, v[1]-1-rang]
    if left_up[0] < 0:
        left_up[0] = 0
    if left_up[1] < 0:
        left_up[1] = 0
    right_down = [v[0]-1+rang, v[1]-1+rang]
    if right_down[0] >= n:
        right_down[0] = n-1
    if right_down[1] >= n:
        right_down[1] = n-1
    for i in range(left_up[0], right_down[0]+1):
        for j in range(left_up[1], right_down[1]+1):
            graph[i][j] += 1

def ice_power(graph, v, rang, n):
    up = v[0]-1-rang
    # for i in range(rang):
    #     for k in range(v[1]-)

def solution(n, m, fires, ices):
    graph = [[0] * n for _ in range(n)]
    for i in range(1, m+1):
        for k in fires:
            fire_power(graph, k, i, n)
        for k in ices:
            ice_power(graph, k, i, n)
    return graph

print(solution(3, 2, [[1, 1]], [[3, 3]]))