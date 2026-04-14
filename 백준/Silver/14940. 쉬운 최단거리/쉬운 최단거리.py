from collections import deque

n,m = map(int, input().split())
g = []
s = []

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1 ,1]

for i in range(n):
  p = list(map(int, input().split()))
  g.append(p)

  if 2 in p:
    s.append(i)
    s.append(p.index(2))

d = [[0] * m for _ in range(n)]

def bfs(r,c):
  q = deque()
  q.append((r,c))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y +dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if g[nx][ny] == 1:
          if d[nx][ny] == 0:
            d[nx][ny] = d[x][y] +1
            q.append((nx, ny))

bfs(s[0], s[1])

for i in range(n):                                                                                   
  for j in range(m):                                                                                 
    if g[i][j] == 1 and d[i][j] == 0:                                                                
      print(-1, end=" ")                                                                             
    else:                                                                                            
      print(d[i][j], end=" ")                                                                        
  print() 