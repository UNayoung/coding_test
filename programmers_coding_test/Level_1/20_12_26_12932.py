def solution(n):
    answer = []
    nToString = str(n)
    for i in reversed(range(0, len(nToString))):
        answer.append(nToString[i])
    for i in range(0, len(answer)):
        answer[i] = int(answer[i])
    return answer

print(solution(12345))