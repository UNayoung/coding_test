def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        temp = ''
        for j in i:
            if skill.find(j) != -1:
                temp += j
        if skill[0:len(temp)] == temp:
            answer += 1
    return answer