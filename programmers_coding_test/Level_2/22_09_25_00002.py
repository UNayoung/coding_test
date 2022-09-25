def search(n, li):
    for i in range(n-1, -1, -1):
        if li[i] != 0:
            return i
    return -1

def solution(cap, n, deliveries, pickups):
    answer = 0
    cur_cap = cap
    cur_dis = n
    while sum(deliveries) or sum(pickups):
        temp = max(search(cur_dis, deliveries), search(cur_dis, pickups))
        cur_dis = temp + 1
        answer += (2 * cur_dis)
        # 택배 내려주기
        for i in range(cur_dis-1, -1, -1):
            if cur_cap == 0:
                break
            if deliveries[i] == 0:
                continue
            if deliveries[i] >= cur_cap:
                deliveries[i] -= cur_cap
                cur_cap = 0
            else:
                cur_cap -= deliveries[i]
                deliveries[i] = 0
        cur_cap = 0
        # 택배 가져오기
        for i in range(cur_dis-1, -1, -1):
            if cur_cap == cap:
                break
            if pickups[i] == 0:
                continue
            if pickups[i] >= (cap-cur_cap):
                pickups[i] -= (cap-cur_cap)
                cur_cap = cap
            else:
                cur_cap += pickups[i]
                pickups[i] = 0
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))