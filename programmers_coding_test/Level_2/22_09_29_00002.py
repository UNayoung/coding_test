from typing import List

new_dic = []

def make(cur, remain, k):
    if remain == "":
        global new_dic
        new_dic.append(cur)
        return
    for i in range(1, min(len(remain), k) + 1):
        make(cur + remain[:i], remain[i:], k)
        make(cur + ".", remain[i:], k)

def solution(k, dic, chat):
    chat_word = chat.split()
    for i in dic:
        make("", i, k)
    dic += new_dic
    for i in range(len(chat_word)):
        if chat_word[i] in dic:
            chat_word[i] = "#" * (len(chat_word[i]))
    return " ".join(chat_word)

print(solution(2, ["a", "b"], "a b c d"))