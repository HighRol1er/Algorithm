import sys
N = int(sys.stdin.readline())

# 오름차순 
arr = []
for _ in range(N):
  age_str, name = sys.stdin.readline().split()
  age = int(age_str) 
  arr.append((age, name))

sorted_arr = sorted(arr, key=lambda x: x[0])
for i in sorted_arr:
  a, n = i
  print(a, n)