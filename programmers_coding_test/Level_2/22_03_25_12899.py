def solution(n):
    answer = ''
    country = [1, 2, 4]
    answer += str((n-1)//3)
    answer += str(country[(n-1)%3])
    return str(int(answer))
