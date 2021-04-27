def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        no_down = 0
        for j in range(i+1, len(prices)):
            if(prices[j] < prices[i]):
                no_down += 1
                break
            no_down += 1
        answer.append(no_down)
    answer.append(0)
    return answer

print(solution([1,2,3,2,3]))