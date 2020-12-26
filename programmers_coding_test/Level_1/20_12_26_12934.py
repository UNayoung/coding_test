def solution(n):
    answer = 0
    temp = pow(n, 1/2)
    if(temp-int(temp)>0):
        return -1
    answer = pow(temp+1, 2)
    return int(answer)

print(solution(121))