import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

max_val = max(numbers)
min_val = min(numbers)

print(min_val, max_val)