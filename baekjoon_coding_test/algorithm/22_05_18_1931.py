def solution():
    n = int(input())
    schedule = [list((map(int, input().split()))) for _ in range(n)]
    schedule.sort(key=lambda x: (x[1], x[0]))
    answer = 1
    temp = schedule[0][1]
    for i in range(1, n):
        if schedule[i][0] >= temp:
            answer += 1
            temp = schedule[i][1]
    print(answer)

solution()