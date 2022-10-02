def nTok(n, k):
    n1, n2 = divmod(n, k)
    if n1 == 0:
        return str(n2)
    else:
        return nTok(n1, k) + str(n2)

def solution(n, k):
    answer = -1
    convert = nTok(n, k)
    print(convert)
    return answer

print(solution(437674, 3))