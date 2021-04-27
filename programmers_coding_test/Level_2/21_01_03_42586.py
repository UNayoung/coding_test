# 기능개발
import math

def solution(progresses, speeds):
    answer = []
    remain_day = []
    for i in range(len(progresses)):
        remain_day.append(math.ceil((100-progresses[i])/speeds[i]))
    big = remain_day[0]
    count = 1
    for i in range(1, len(remain_day)+1):
        if(i == len(remain_day)):
            answer.append(count)
            break
        if(remain_day[i] > big):
            answer.append(count)
            big = remain_day[i]
            count = 1
        else:
            count += 1
    return answer

# print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 소수점 올림 - math.ceil(i)
# 소수점 내림 - math.floor(i)