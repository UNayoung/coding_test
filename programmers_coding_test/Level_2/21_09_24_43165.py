answer = []

def search(arr, sum):
    if len(arr) == 0:
        answer.append(sum)
        return
    else:
        temp = arr[0]
        search(arr[1:len(arr)], sum - temp)
        search(arr[1:len(arr)], sum + temp)

def solution(numbers, target):
    search(numbers, 0)
    return answer.count(target)

print(solution([1, 1, 1, 1, 1], 3))

# list에서 빼는 방식으로 sum 이랑 list만 매개변수로
