import sys

input = sys.stdin.readline

m = int(input())

# set
s = set()

for _ in range(m):
  token = input().replace(" ", "")

  if "add" in token:
    s.add(int(token[3:]))
  elif "remove" in token:
    s.discard(int(token[6:]))
  elif "check" in token:
    num = int(token[5:])
    if num in s:
      print(1)
    else:
      print(0)
  elif "toggle" in token:
    num = int(token[6:])
    if num in s:
      s.remove(num)
    else:
      s.add(num)
  elif "all" in token:
    s = set(range(1,21))
  elif "empty" in token:
    s = set()



