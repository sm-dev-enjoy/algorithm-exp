import heapq

def solution(k, score):
    result = []
    top_k = []
    
    for s in score:
        if len(top_k) < k:
            heapq.heappush(top_k, s)
        elif top_k[0] < s:
            heapq.heappop(top_k)
            heapq.heappush(top_k, s)
        result.append(top_k[0])
    
    return result
