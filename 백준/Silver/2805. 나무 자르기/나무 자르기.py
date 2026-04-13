import sys
input = sys.stdin.readline

n,m = map(int, input().split())
t = list(map(int, input().split()))

l = 0 
h = max(t)

while l <= h: 
  mid = (l + h) // 2
  s = sum(i - mid for i in t if i > mid)
  
  if s >= m:
    l = mid + 1
  elif s < m:
    h = mid - 1 

print(h)