def solution(arr, divisor):
    answer = []
    dup = 0
    for i in arr:
        if(i%divisor==0):
            dup=dup+1
            answer.append(i)
    answer.sort()
    if(dup==0):
        return [-1]
    return answer

print(solution([3,2,6], 10))