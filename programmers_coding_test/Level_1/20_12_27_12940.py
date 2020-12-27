def solution(n, m):
    answer = []
    if(n<=m):
        for i in reversed(range(1, n+1)):
            if(n%i==0 and m%i==0):
                answer.append(i)
                temp = i*(n/i)*(m/i)
                answer.append(int(temp))
                return answer
    else:
        for i in reversed(range(1, m+1)):
            if (n % i == 0 and m % i == 0):
                answer.append(i)
                temp = i * (n / i) * (m / i)
                answer.append(int(temp))
                return answer

print(solution(24, 48))