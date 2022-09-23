lion = []

def find(arr, info, n, cur, sum_arr, score):
    if sum(arr) > n or cur < 0 or sum_arr <= score:
        return
    if sum(arr) == n:
        global lion
        lion.append(arr)
        return
    temp = arr[:]
    temp[cur] = info[cur] + 1
    find(temp, info[:], n, cur-1, sum_arr+cur*temp[cur], score)
    temp = arr[:]
    temp[cur] = 0
    find(temp, info[:], n, cur-1, sum_arr+cur*temp[cur], score)

def solution(n, info):
    answer = []
    temp = 0
    for i in range(11):
        temp += (info[i] * (10-i))
    find([0,0,0,0,0,0,0,0,0,0,0], info, n, 10, 0, temp)
    print(lion)
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
