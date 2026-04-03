'''
점 N개 
x 좌표가 증가하는 순으로 x 좌표가 같으면 y 오름 차순으로 정렬 
'''
import sys
N = int(sys.stdin.readline())

arr = []
for _ in range(N):
  x, y = map(int, sys.stdin.readline().split())
  arr.append((x,y))

sorted_arr = sorted(arr)

for i in sorted_arr:
  x, y = i
  print(x,y)
