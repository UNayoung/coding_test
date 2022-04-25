def solution(rows, columns, queries):
    answer = []
    matrix = []
    digit = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(digit)
            digit += 1
        matrix.append(temp)
    print(matrix)
    for i in queries:
        print(i)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))