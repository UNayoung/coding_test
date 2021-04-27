def solution(nums):
    my_set = list(set(nums))
    if(len(nums)//2<=len(my_set)):
        answer = len(nums)//2
    else:
        answer = len(my_set)
    return answer

print(solution([3,3,3,2,2,2]))