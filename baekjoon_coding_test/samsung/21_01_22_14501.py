arr = [list(map(int, input().split())) for _ in range(int(input()))]
day = len(arr)
pay = []

def solution(sum, location):
    if(location == day):
        pay.append(sum)
        return
    if((location+arr[location][0]) > day):
        solution(sum, location+1)
    else:
        if(arr[location][0] == 1):
            solution(sum+arr[location][1], location+1)
        else:
            solution(sum, location+1)
            solution(sum+arr[location][1], location+arr[location][0])

solution(0, 0)
print(max(pay))