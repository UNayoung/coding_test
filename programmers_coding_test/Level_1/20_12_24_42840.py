def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    result_one = 0
    for i in range(0, len(answers)):
        if(answers[i]==one[i%5]):
            result_one = result_one+1
    print(result_one)
    result_two = 0
    for i in range(0, len(answers)):
        if(answers[i]==two[i%8]):
            result_two = result_two+1
    print(result_two)
    result_three = 0
    for i in range(0, len(answers)):
        if(answers[i]==three[i%10]):
            result_three = result_three+1
    print(result_three)
    order=[]
    order.append(result_one)
    order.append(result_two)
    order.append(result_three)
    print(order)
    m = max(order)
    answer = [i for i, j in enumerate(order) if j==m]
    for i in range(0, len(answer)):
        answer[i]=answer[i]+1
    return answer

print(solution([1,3,2,4,2]))