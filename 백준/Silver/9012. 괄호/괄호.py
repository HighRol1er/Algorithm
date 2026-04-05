N = int(input())

for _ in range(N):
  x = input()
  stack = []
  is_vps = True

  for i in x:
    if i == '(':
      stack.append(i)
    elif i == ')':
      if stack:
        stack.pop()
      else:
        is_vps = False
        break
  if is_vps and not stack:
    print('YES')
  else:
    print('NO')