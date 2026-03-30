import sys 

input_data = sys.stdin.readline

while True:
  line = input_data().split()
  if not line: break

  A, B = map(int, line)

  if A == 0 and B == 0:
    break

  print(A + B)