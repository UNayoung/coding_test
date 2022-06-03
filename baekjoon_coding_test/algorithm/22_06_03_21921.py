def solution():
    n, x = map(int, input().split())
    visit = list(map(int, input().split()))
    answer = []
    for i in range(n-x+1):
        temp = 0
        for k in range(i, i+x):
            temp += visit[k]
        answer.append(temp)
    if max(answer) == 0:
        print('SAD')
        return
    print(max(answer))
    print(answer.count(max(answer)))

solution()