def solution():
    answer = 0
    sound = list(input())
    max_quack = len(sound) // 5
    for _ in range(max_quack):
        temp = []
        for i in range(len(sound)):
            # print(temp)
            # print(sound[i])
            if sound[i] == 'q':
                if not temp or (temp and temp[-1][1] == 'k'):
                    temp.append([i, sound[i]])
            if sound[i] == 'u' and temp and temp[-1][1] == 'q':
                temp.append([i, sound[i]])
            if sound[i] == 'a' and temp and temp[-1][1] == 'u':
                temp.append([i, sound[i]])
            if sound[i] == 'c' and temp and temp[-1][1] == 'a':
                temp.append([i, sound[i]])
            if sound[i] == 'k' and temp and temp[-1][1] == 'c':
                temp.append([i, sound[i]])
        if temp and len(temp) % 5 == 0:
            answer += 1
            for i in temp:
                sound[i[0]] = 'o'
    if answer == 0:
        print(-1)
        return
    print(answer)

solution()