import sys
from collections import deque

def bfs(graph, v):
    queue = deque([v])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]

def solution():
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(graph)

solution()