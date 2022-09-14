def solution(queue1, queue2):
    answer = 0
    while True:
        sum1 = sum(queue1)
        sum2 = sum(queue2)
        if sum1 == sum2:
            break
        if sum1 > sum2:
            temp = queue1.pop(0)
            queue2.append(temp)
        else:
            temp = queue2.pop(0)
            queue1.append(temp)
        answer += 1
    return answer

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))