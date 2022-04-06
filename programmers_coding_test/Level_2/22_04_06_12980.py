def solution(n):
    ans = 1
    while True:
        if n == 1:
            break
        q, r = divmod(n, 2)
        n = q
        if r == 1:
            ans += 1
    return ans

print(solution(5))