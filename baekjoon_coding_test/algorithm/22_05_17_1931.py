def solution():
    n = int(input())
    schedule = []
    result = 0

    for i in range(n):
        start, end = map(int, input().split())
        temp = [k for k in range(start, end)]
        exist = 0
        for j in range(1, len(schedule)):
            if set(schedule[j-1]) & set(temp) != set():
                exist = 1
                if set(schedule[j]) & set(temp) != set():
                    break
                else:
                    if len(temp) < len(schedule[j-1]):
                        schedule.insert(j)
                        del schedule[j-1]
                        break
        if exist == 0:
            result += 1
            schedule.append(temp)
    print(result)

solution()