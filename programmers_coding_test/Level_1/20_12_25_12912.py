def solution(a, b):
    answer = 0
    if(a<=b):
        for i in range(a, b+1):
            answer=answer+i
    else:
        for i in range(a, b-1, -1):
            answer=answer+i
    return answer

print(solution(5, 3))