import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    arr = []
    p_arr = []
    prime = []
    for i in numbers:
        arr.append(i)
    for i in range(1, len(arr)+1):
        temp = list(map(''.join, itertools.permutations(arr, i)))
        p_arr.extend(temp)
    for i in p_arr:
        if(is_prime(int(i)) == True):
            prime.append(int(i))
    prime_set = set(prime)
    answer = len(prime_set)
    return answer

print(solution("011"))

# 모든 조합을 다 찾은다음
# 각각 숫자로 바꿔서 소수판별
# 0으로 시작하는 것 제거 & 중복제거
# 몇개인지 출력