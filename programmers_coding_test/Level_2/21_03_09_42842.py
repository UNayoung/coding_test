def solution(brown, yellow):
    answer = []
    set = []
    for i in range(1, brown+yellow+1):
        if((brown+yellow)%i==0):
            set.append(i)
    set = set[len(set)//2:len(set)-1]
    for i in set:
        y = brown+yellow-(i*2+((brown+yellow)//i-2)*2)
        if(y==yellow):
            answer.append(i)
            answer.append((brown+yellow)//i)
            break
    return answer

print(solution(24, 24))