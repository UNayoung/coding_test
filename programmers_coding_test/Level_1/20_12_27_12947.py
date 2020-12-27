def solution(x):
    answer = True
    toString = str(x)
    toList = list(toString)
    for k in range(0, len(toList)):
        toList[k] = int(toList[k])
    sum = 0
    for i in toList:
        sum+=i
    if(x%sum!=0):
        return False
    return answer

print(solution(11))