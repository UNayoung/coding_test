def solution(n):
    answer = []
    graph = [[0]*i for i in range(1, n+1)]
    start = n
    nx = 1
    ny = 0
    count = 1
    for i in range(n-1, 0, -3):
        nx -= 1
        for j in range(i):
            for _ in range(3):
                nx -= 1
                ny = graph[nx].index(0)
                graph[nx][ny] = count
                count += 1

    return answer

print(solution(6))