import sys
input = sys.stdin.readline
n,m = map(int, input().split())

g = [[] for _ in range(n + 1)]  

connection = 0 

for i in range(m):
  u,v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

visited = [False] * (n + 1)

def dfs(v):
  stack = [v]
  visited[v] = True

  while stack:
    p = stack.pop()
    for j in g[p]:
      if not visited[j]:
        visited[j] = True
        stack.append(j)


for k in range(1,n +1):
  if visited[k] == False:
    connection += 1
    dfs(k)

print(connection)
