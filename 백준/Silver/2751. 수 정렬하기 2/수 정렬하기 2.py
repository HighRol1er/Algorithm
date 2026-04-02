import sys
N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    i = int(sys.stdin.readline())
    arr.append(i)

sorted_arr = sorted(arr)

for j in sorted_arr:
    print(j)