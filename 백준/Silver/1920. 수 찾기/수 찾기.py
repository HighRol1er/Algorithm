'''
점 N개 
x 좌표가 증가하는 순으로 x 좌표가 같으면 y 오름 차순으로 정렬 
한번 틀림 
틀린코드는 아래에 주석으로 작성 
'''
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

def b_search(arr, target):
  lo, hi = 0, len(arr) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target: 
      lo = mid + 1
    else: 
      hi = mid - 1
  return False

for i in B: 
  print(1 if b_search(A,i) else 0)

'''
점 N개 
x 좌표가 증가하는 순으로 x 좌표가 같으면 y 오름 차순으로 정렬 
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
  if i in A:
    print(1)
  else:
    print(0)

'''