import sys

def solution():
    input = sys.stdin.readline
    r, c, q = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(map(int, input().split())))
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        answer = 0
        for i in range(r1 - 1, r2):
            answer += sum(graph[i][c1-1:c2])
        area = (r2 - r1 + 1) * (c2 - c1 + 1)
        print(answer // area)

solution()