# 그냥 깊이가 4인지 찾는 문제
import sys
from collections import defaultdict, deque

def bfs(graph, visited, v, depth):
    visited[v] = True
    queue = deque([v])
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                depth[i] = depth[temp] + 1
        print(depth)

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = defaultdict(list)
    visited = defaultdict(bool)
    depth = defaultdict(int)
    for _ in range(m):
        r1, r2 = map(int, input().split())
        graph[r1].append(r2)
        graph[r2].append(r1)
    bfs(graph, visited, 0, depth)
    print(depth)
    if max(depth.values()) == (n - 1):
        print(1)
    else:
        print(0)

solution()