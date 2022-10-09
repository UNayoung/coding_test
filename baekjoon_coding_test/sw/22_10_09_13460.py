import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by)])
    graph[rx][ry] = 0
    while queue:
        temp = queue.popleft()
        print(temp)
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if graph[nx][ny] == "#" or graph[nx][ny] == (graph[temp[0]][temp[1]] + 1):
                continue
            goal_r = False
            goal_b = False
            back = False
            while True:
                if graph[nx][ny] == "#":
                    nx -= dx[i]
                    ny -= dy[i]
                    if back:
                        nx -= dx[i]
                        ny -= dy[i]
                    break
                if graph[nx][ny] == "O":
                    goal_r = True
                    break
                if nx == temp[2] and ny == temp[3]:
                    back = True
                graph[nx][ny] = graph[temp[0]][temp[1]] + 1
                nx += dx[i]
                ny += dy[i]
            nx2 = temp[2] + dx[i]
            ny2 = temp[3] + dy[i]
            back = False
            while True:
                if graph[nx2][ny2] == "#":
                    nx2 -= dx[i]
                    ny2 -= dy[i]
                    if back:
                        nx2 -= dx[i]
                        ny2 -= dy[i]
                    break
                if graph[nx2][ny2] == "O":
                    goal_b = True
                    break
                if nx2 == temp[0] and ny2 == temp[1]:
                    back = True
                nx2 += dx[i]
                ny2 += dy[i]
            if goal_b:
                continue
            if goal_r:
                return graph[temp[0]][temp[1]] + 1
            if (graph[temp[0]][temp[1]] + 1) > 10:
                print(-1)
                exit(0)
            queue.append((nx, ny, nx2, ny2))
    print(-1)
    exit(0)

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = []
    rx = -1
    ry = -1
    bx = -1
    by = -1
    for i in range(n):
        temp = list(input().strip())
        graph.append(temp)
        if "R" in temp:
            rx = i
            ry = temp.index("R")
        if "B" in temp:
            bx = i
            by = temp.index("B")
    print(bfs(graph, rx, ry, bx, by))

solution()