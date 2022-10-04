def nTok(n, k):
    n1, n2 = divmod(n, k)
    if n1 == 0:
        return str(n2)
    else:
        return nTok(n1, k) + str(n2)

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def solution(n, k):
    answer = 0
    convert = nTok(n, k)
    arr = convert.split("0")
    for i in arr:
        if i != '' and isPrime(int(i)):
            answer += 1
    return answer

print(solution(110011, 10))