import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if a == b:
                    continue
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    print(graph)

solution()