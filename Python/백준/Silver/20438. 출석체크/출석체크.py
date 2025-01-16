import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split()) 

sleep = set(map(int, input().split()))
code = set(map(int, input().split()))

m_tuple = [] # 범위 

for _ in range(m):
  s, e = map(int, input().split())
  m_tuple.append((s,e))

# print(sleep)
# print(code)
# print(sleep - code)

# 출석 학생 표시
checked = [0] * (n * 3)
for q in (code - sleep) : # 3,5만 남음
  for i in range(q, n + 3, q): # start, end, step 스텝을 왜 넣지? 
    if i not in sleep:
      checked[i] = 1

# 미참석자 수 합치는 단계 => 누적합? 
attend = [0] * (n * 3)
for i in range(3, n + 3):
  if not checked[i]:
    attend[i] = attend[i - 1] + 1
  else: 
    attend[i] = attend[i - 1]

ans = []

for s,e in m_tuple:
  ans.append(attend[e] - attend[s - 1])

for a in ans:
  print(a)
