import sys
from collections import deque, defaultdict

def dfs(graph):
    answer = 0
    visited = defaultdict(bool)
    queue = deque([1])
    visited[1] = True
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True
            answer += 1
    return answer

def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(dfs(graph))

solution()