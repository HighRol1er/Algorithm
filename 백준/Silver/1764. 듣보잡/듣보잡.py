import sys

input = sys.stdin.readline
n, m = map(int, input().split())

no_listen = set()
for _ in range(n):
    no_listen.add(input().strip())

no_see = set()
for _ in range(m):
    no_see.add(input().strip())

intersection = sorted(list(no_listen & no_see))

print(len(intersection))
for i in intersection:
  print(i)