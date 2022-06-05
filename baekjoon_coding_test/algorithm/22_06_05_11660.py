import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(1, n):
        graph[0][i] += graph[0][i-1]
    for i in range(1, n):
        graph[i][0] += graph[i-1][0]
    for i in range(1, n):
        for j in range(1, n):
            graph[i][j] += (graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1])
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 1 and y1 == 1:
            print(graph[x2-1][y2-1])
            continue
        if x1 == 1:
            print(graph[x2-1][y2-1] - graph[x1-2][y2-1])
            continue
        if y1 == 1:
            print(graph[x2-1][y2-1] - graph[x2-1][y1-2])
            continue
        print(graph[x2-1][y2-1] - graph[x1-2][y2-1] - graph[x2-1][y1-2] + graph[x1-2][y1-2])

solution()

# 4 3

# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

# 1 3 6 10
# 3 8 15 24
# 6 15 27 42
# 10 24 42 64

# 2 2 3 4
# 3 4 3 4
# 1 1 4 4
