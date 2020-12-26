def solution(n):
    answer = ''
    watermelon = ["수", "박"]
    for i in range(0, n):
        answer=answer+watermelon[i%2]
    return answer

print(solution(4))