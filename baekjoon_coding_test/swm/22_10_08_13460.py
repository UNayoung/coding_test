import sys
from collections import deque

def bfs(graph, v):
    queue = deque([v])
    graph[v[0]][v[1]] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if graph[nx][ny] == "." or graph[nx][ny] == "R" or graph[nx][ny] == "B":
                red = -1
                blue = -1
                order = 0
                while True:
                    if graph[nx][ny] == "#":
                        queue.append([nx-dx[i], ny-dy[i]])
                        break
                    if graph[nx][ny] == "R":
                        red = order
                    if graph[nx][ny] == "B":
                        blue = order
                    graph[nx][ny] = graph[temp[0]][temp[1]] + 1
                    nx += dx[i]
                    ny += dy[i]
                    order += 1
                print(graph, red, blue)
                if red != -1:
                    if blue != -1 and blue < red:
                        print(-1)
                        exit(0)
                    return graph[temp[0]][temp[1]] + 1
    print(-1)
    exit(0)

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    hole = []
    graph = []
    for i in range(n):
        temp = list(input().strip())
        if "O" in temp:
            hole.append(i)
            hole.append(temp.index("O"))
        graph.append(temp)
    result = bfs(graph, hole)
    if result <= 10:
        print(result)
        exit(0)
    print(-1)
    exit(0)

solution()