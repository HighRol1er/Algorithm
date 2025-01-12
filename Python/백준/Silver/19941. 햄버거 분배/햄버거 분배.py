import sys
input = sys.stdin.readline

n, k = map(int,input().split())
table = list(input().strip()) 

cnt = 0 

for i in range(n): 
  if table[i] == "P":
    start = max(0, i - k)
    end = min(n, i + k + 1)
    for j in range(start, end): 
      if table[j] == "H":
        table[j] = "D"
        cnt += 1
        break

print(cnt)