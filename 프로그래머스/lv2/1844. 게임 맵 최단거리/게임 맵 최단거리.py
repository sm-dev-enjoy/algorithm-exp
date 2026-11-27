from collections import deque

def solution(maps):
    
    dy = [0,1,0,-1] # 행
    dx = [1,0,-1,0] # 열
    n = len(maps)
    m = len(maps[0])
    queue = deque([(0,0,1)])        
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        y,x,dist = queue.popleft()
        if y == n-1 and x == m-1:
            return dist
        
        for i in range(4):
            ny = y + dy[i] 
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny,nx,dist+1))
    return -1
