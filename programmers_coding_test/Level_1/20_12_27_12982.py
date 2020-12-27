def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if(i>budget):
            break
        if(i<=budget):
            answer+=1
            budget-=i
    return answer

print(solution([2,2,3,3], 10))