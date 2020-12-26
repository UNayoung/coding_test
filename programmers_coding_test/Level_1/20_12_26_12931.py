def solution(n):
    answer = 0
    nToString = str(n)
    for i in nToString:
        answer+=int(i)
    return answer

print(solution(987))