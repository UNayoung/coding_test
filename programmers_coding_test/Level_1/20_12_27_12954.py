def solution(x, n):
    answer = []
    for i in range(1, n+1):
        temp = x*i
        answer.append(temp)
    return answer

print(solution(-4, 3))