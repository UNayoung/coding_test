from collections import defaultdict, deque

def bfs(graph):
    queue = deque(['ICN'])
    answer = ['ICN']
    while queue:
        current = queue.popleft()
        if not graph[current]:
            break
        next = graph[current].pop(0)
        queue.append(next)
        answer.append(next)
    return answer

def solution(tickets):
    graph = defaultdict(list)
    for i in tickets:
        graph[i[0]].append(i[1])
    for i in graph:
        graph[i].sort()
    return bfs(graph)