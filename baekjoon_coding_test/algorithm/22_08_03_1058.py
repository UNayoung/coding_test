import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    INF = int(1e9)
    graph = [[INF] * n for _ in range(n)]
    answer = -1
    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 0
    for i in range(n):
        temp = list(input().strip())
        for j in range(len(temp)):
            if temp[j] == 'Y':
                graph[i][j] = 1
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    print(graph)
    for i in graph:
        if max(i) > answer:
            answer = max(i)
    print(answer)

solution()