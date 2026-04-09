N = int(input())
time = list(map(int, input().split()))

time.sort()

total_time = 0

for i in range(1, N + 1):
  t_sum = sum(time[:i])
  total_time += t_sum

print(total_time)