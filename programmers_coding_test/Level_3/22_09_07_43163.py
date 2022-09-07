answer = 51

def dfs(words, current, target, count):
    global answer
    if current == target:
        answer = min(answer, count)
        return
    if not words:
        answer = 0
        return
    length_words = len(words)
    for i in range(length_words):
        if len(set(list(words[i])) - set(list(current))) == 1:
            dfs(words[:i]+words[i+1:length_words], words[i], target, count+1)

def solution(begin, target, words):
    dfs(words, begin, target, 0)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))