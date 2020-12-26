def solution(strings, n):
    answer = []
    for k in strings:
        answer.append(k)
    for i in range(len(answer)-1):
        for j in range(len(answer)-i-1):
            if(answer[j][n]>answer[j+1][n]):
                temp = answer[j]
                answer[j] = answer[j+1]
                answer[j+1] = temp
            elif(answer[j][n]==answer[j+1][n]):
                if(answer[j]>answer[j+1]):
                    temp = answer[j]
                    answer[j] = answer[j+1]
                    answer[j+1] = temp
    return answer

print(solution(["abce", "abcd", "cdx"], 2))