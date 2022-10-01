from collections import defaultdict
from typing import List

def binSearch(target):
    left = 1
    right = 17
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if pow(2, mid) == target:
            answer = pow(2, mid)
            break
        elif pow(2, mid) > target:
            right = mid - 1
            answer = pow(2, mid)
        else:
            left = mid + 1
    return answer

def solution(queries) -> int:
    answer = 0
    graph = defaultdict(list)
    for i in queries:
        if len(graph[i[0]]) == 0:
            graph[i[0]] = [0, 0, 0]
        temp = graph[i[0]][1] + i[1]
        if temp > graph[i[0]][0]:
            graph[i[0]][2] += graph[i[0]][1]
            graph[i[0]][0] = binSearch(temp)
        graph[i[0]][1] = temp
    for i in graph:
        answer += graph[i][2]
    return answer

print(solution([[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]))