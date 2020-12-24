def solution(board, moves):
    answer = 0
    result = []
    for i in moves:
        for j in range(0, len(board)):
            if(board[j][i-1]!=0):
                result.append(board[j][i-1])
                board[j][i - 1] = 0
                if(len(result)>1):
                    if(result[len(result)-1]==result[len(result)-2]):
                        answer=answer+2
                        result.pop()
                        result.pop()
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))