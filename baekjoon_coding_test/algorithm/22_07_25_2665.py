import sys
from collections import deque

def bfs(graph, visited, v, n):
    queue = deque([v])
    x, y = v
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

def solution():
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(input().strip()))
    
    print(graph)

solution()