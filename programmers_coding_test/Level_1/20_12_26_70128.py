def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        temp = a[i]*b[i]
        answer+=temp
    return answer

print(solution([-1,0,1], [1,0,-1]))