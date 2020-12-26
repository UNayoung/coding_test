def solution(n):
    answer = 0
    nToString = str(n)
    ToList = list(nToString)
    for i in range(0, len(ToList)):
        ToList[i] = int(ToList[i])
    ToList.sort(reverse=True)
    for i in range(0, len(ToList)):
        ToList[i] = str(ToList[i])
    answer = ''.join(ToList)
    answer = int(answer)
    return answer

print(solution(118372))