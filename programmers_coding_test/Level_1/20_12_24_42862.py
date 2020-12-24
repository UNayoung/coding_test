def solution(n, lost, reserve):
    lost_real = list(set(lost) - set(reserve))
    reserve_real = list(set(reserve) - set(lost))
    answer = n - len(lost_real)
    com = []
    for i in reserve_real:
        com.append(0)
    for i in lost_real:
        for j in range(0, len(reserve_real)):
            if(reserve_real[j]==i-1 and com[j]==0):
                answer=answer+1
                com[j]=1
                break
            if(reserve_real[j]==i+1 and com[j]==0):
                answer=answer+1
                com[j]=1
                break
    return answer

print(solution(3, [3], [1]))