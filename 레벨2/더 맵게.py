import heapq

def solution(scoville, K):
    heap = []

    for value in scoville:
        heapq.heappush(heap, value)

    # 조건1. 최소값이 K 이상이면 탈출
    # 조건2. 힙의 원소가 2이하면 탈출
    ret = 0
    while len(heap) >= 2:
        one = heapq.heappop(heap)
        if one >= K:
            break
        second = heapq.heappop(heap)
        heapq.heappush(heap, one + (second * 2))
        ret += 1

    min = heapq.heappop(heap)
    if min < K:
        ret = -1

    return ret