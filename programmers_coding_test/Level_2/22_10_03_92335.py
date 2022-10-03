def nTok(n, k):
    n1, n2 = divmod(n, k)
    if n1 == 0:
        return str(n2)
    else:
        return nTok(n1, k) + str(n2)

def isPrime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

def solution(n, k):
    answer = 0
    convert = nTok(n, k)
    arr = convert.split("0")
    for i in arr:
        if i == '':
            continue
        if isPrime(int(i)):
            answer += 1
    return answer

print(solution(110011, 10))