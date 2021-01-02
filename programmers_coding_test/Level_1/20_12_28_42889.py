# def solution(N, stages):
#     rate = []
#     for i in range(1, N+1):
#         noclear = stages.count(i)
#         come = sum(map(lambda x: x >= i, stages))
#         rate.append([i, noclear/come])
#     rate.sort(key=lambda x:x[1], reverse=True)
#     for i in range(0, N):
#         rate[i] = rate[i][0]
#     return rate

def solution(N, stages):
    fail_rate = {}
    total_user = len(stages)
    for stage in range(1, N+1):
        if total_user != 0:
            fail_user = stages.count(stage)
            fail_rate[stage] = fail_user / total_user
            total_user -= fail_user
        else:
            fail_rate[stage] = 0
    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# 런타임 에러 발생