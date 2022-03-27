def solution(n):
    answer = ""
    otf = ['1', '2', '4']
    while n:
        tmp = (n - 1) % 3
        n = (n - 1) // 3
        answer += otf[tmp]
    return answer[::-1]

print(solution(7))