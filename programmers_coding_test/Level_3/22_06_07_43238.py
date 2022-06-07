def solution(n, times):
    current = [0, 0]
    for _ in range(n):
        temp1 = [current[i] + times[i] for i in range(len(times))]
        temp2 = temp1.index(min(temp1))
        current[temp2] = temp1[temp2]
    return max(current)

print(solution(6, [7, 10]))