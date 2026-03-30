import sys

numbers = [int(sys.stdin.readline()) for _ in range(9)]

max_value = max(numbers)
target_index = numbers.index(max_value)
print(max_value)
print(target_index + 1)