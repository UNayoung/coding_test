def solution(n):
    answer = ""
    otf = ['1', '2', '4']
    while n:
        n, tmp = divmod(n - 1, 3)
        answer += otf[tmp]
    return answer[::-1]

print(solution(7))