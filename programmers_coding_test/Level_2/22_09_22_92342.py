lion = []

def find(arr, info, n, cur):
    if sum(arr) > n or cur < 0:
        return
    if sum(arr) == n:
        global lion
        lion.append(arr)
    temp = info[:]
    temp[cur] = info[cur] + 1
    find(temp, info[:], n, cur-1)
    temp = info[:]
    temp[cur] = 0
    find(temp, info[:], n, cur-1)

def solution(n, info):
    answer = []
    find([0,0,0,0,0,0,0,0,0,0,0], info, n, 10)
    print(lion)
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
