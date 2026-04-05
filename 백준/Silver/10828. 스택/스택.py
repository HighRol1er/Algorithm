N = int(input())

msg = []
for _ in range(N):
  m = input()
  msg.append(m.replace(" ", ""))

stack = []
for i in msg:
  if 'push' in i:
    stack.append(i[4:])
  elif i == 'pop':
    if stack:
      n = stack.pop()
      print(n)
    else:
      print(-1)
  elif i == 'size':
    print(len(stack))
  elif i == 'empty':
    if stack:
      print(0)
    else: 
      print(1)
  elif i == 'top':
    l = len(stack)
    if l == 0:
      print(-1)
    else:
      print(stack[l-1])