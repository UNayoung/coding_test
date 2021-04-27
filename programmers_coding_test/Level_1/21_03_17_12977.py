from itertools import combinations

def is_prime(num):
    n = int(num**0.5)
    for i in range(2, n+1):
        if(num%i == 0):
            return False
    return True

def solution(nums):
    answer = 0
    nums_c = list(combinations(nums, 3))
    for i in nums_c:
        if(is_prime(sum(i)) == True):
            answer += 1
    return answer

print(solution([1,2,3,4]))