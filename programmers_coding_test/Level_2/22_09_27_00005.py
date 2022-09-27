from collections import defaultdict

def solution(commands):
    answer = []
    graph = [[""]*51 for _ in range(51)]
    merge_dict = defaultdict(list)
    count = 1
    for i in commands:
        temp = i.split()
        if temp[0] == "UPDATE":
            if len(temp) == 4:
                r, c = int(temp[1]), int(temp[2])
                if type(graph[r][c]) != int:
                    graph[r][c] = temp[3]
                else:
                    merge_dict[graph[r][c]][4] = temp[3]
            else:
                for a in range(1, 51):
                    for b in range(1, 51):
                        if graph[a][b] == temp[1]:
                            graph[a][b] = temp[2]
            continue
        if temp[0] == "MERGE":
            r1, c1, r2, c2 = int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4])
            left_x, left_y, right_x, right_y = min(r1, r2), min(c1, c2), max(r1, r2), max(c1, c2)
            value = graph[r1][c1]
            if type(graph[r2][c2]) == int:
                m1, m2, m3, m4, v1 = merge_dict[graph[r2][c2]]
                left_x, left_y, right_x, right_y = min(left_x, m1), min(left_y, m2), max(right_x, m3), max(right_y, m4)
                value = v1
            if type(graph[r1][c1]) == int:
                m1, m2, m3, m4, v1 = merge_dict[graph[r1][c1]]
                left_x, left_y, right_x, right_y = min(left_x, m1), min(left_y, m2), max(right_x, m3), max(right_y, m4)
                value = v1
            merge_dict[count] = [left_x, left_y, right_x, right_y, value]
            for a in range(left_x, right_x+1):
                for b in range(left_y, right_y+1):
                    graph[a][b] = count
            count += 1
            continue
        if temp[0] == "UNMERGE":
            r, c = int(temp[1]), int(temp[2])
            left_x, left_y, right_x, right_y, value = merge_dict[graph[r][c]]
            for a in range(left_x, right_x+1):
                for b in range(left_y, right_y+1):
                    graph[a][b] = ""
            graph[r][c] = value
            continue
        if temp[0] == "PRINT":
            r, c = int(temp[1]), int(temp[2])
            if graph[r][c] == "":
                answer.append("EMPTY")
            elif type(graph[r][c]) != int:
                answer.append(graph[r][c])
            else:
                answer.append(merge_dict[graph[r][c]][4])
            continue
    return answer

print(solution(
["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))