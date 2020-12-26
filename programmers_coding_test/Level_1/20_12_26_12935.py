def solution(arr):
    answer = arr
    temp = min(arr)
    answer.remove(temp)
    if(answer==[]):
        return [-1]
    return answer

print(solution([4,3,2,1]))