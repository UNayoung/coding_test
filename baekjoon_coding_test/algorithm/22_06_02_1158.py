from collections import deque

def solution():
    n, k = map(int, input().split())
    queue = deque([i for i in range(1, n+1)])
    answer = []
    while queue:
        queue.rotate(-k)
        answer.append(queue.pop())
    print("<" + ', '.join([str(answer[i]) for i in range(n)]) + ">")

solution()