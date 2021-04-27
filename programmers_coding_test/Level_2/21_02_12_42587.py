def solution(priorities, location):
    answer = 0
    arr = []
    new_arr = []
    for i in range(len(priorities)):
        arr.append([i, priorities[i]])
    while(True):
        if(len(arr) == 1):
            arr.pop(0)
            break
        for i in range(1, len(arr)):
            print(arr[i][1])
            if(arr[0][1]<arr[i][1]):
                arr.append(arr[0])
                arr.pop(0)
                break
            else:
                new_arr.append(arr[0])
                arr.pop(0)
    for i in range(len(new_arr)):
        if(new_arr[i][1] == location):
            answer = i+1
    return answer

print(solution([1,1,9,1,1,1], 0))