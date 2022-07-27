from collections import defaultdict
import sys

def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

def solution():
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline
    n, m = map(int, input().split())
    answer = 0
    graph = defaultdict(list)
    visited = defaultdict(bool)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        if not visited[i]:
            answer += 1
            dfs(graph, visited, i)
    print(answer)

solution()