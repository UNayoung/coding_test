from collections import defaultdict, deque
import sys

def bfs(graph, visited, v):
    visited[v] = True
    queue = deque([v])
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if len(graph[i]) >= 3:
                return i
            if not visited[i]:
                # print(i)
                queue.append(i)
                visited[i] = True

def bfs_dist(graph, visited, v, distance):
    visited[v] = False
    queue = deque([v])
    dist = 1
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if visited[i]:
                queue.append(i)
                visited[i] = False
                distance[i] = dist
                dist += 1

def solution():
    input = sys.stdin.readline
    n = int(input())
    stations = defaultdict(list)
    distance = [0]
    visited = defaultdict(bool)
    for _ in range(n):
        distance.append(0)
        a, b = map(int, input().split())
        stations[a].append(b)
        stations[b].append(a)
    print(stations)
    for i in range(1, n + 1):
        if len(stations[i]) == 1:
            temp = bfs(stations, visited, i)
            print(visited)
            bfs_dist(stations, visited, temp, distance)
    distance.pop(0)
    print(*distance)

solution()

# 1로 끝나는게 있으면 검사
