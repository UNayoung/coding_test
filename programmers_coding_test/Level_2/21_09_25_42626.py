import heapq

def solution(scoville, K):
    answer = 0
    arr = []
    for i in scoville:
        heapq.heappush(arr, i)
    while arr[0] < K:
        try:
            heapq.heappush(arr, heapq.heappop(arr) + (heapq.heappop(arr) * 2))
        except IndexError:
            return -1
        answer += 1
    return answer

print(solution([1, 2, 9, 3, 10, 12], 7))

# heappop 하면 제일 작은애 나옴