def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        temp = []
        for j in range(0, len(arr1[i])):
            sum = arr1[i][j] + arr2[i][j]
            temp.append(sum)
        answer.append(temp)
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))