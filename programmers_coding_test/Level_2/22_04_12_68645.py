def solution(n):
    answer = []
    list = dict()
    for i in range(1, n+1):
        list[i] = []
        for j in range(i):
            list[i].append(0)
    cur = 1
    return answer

print(solution(5))