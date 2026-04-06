n = int(input())

stack = []
op = []
temp = 1
possible = True

for _ in range(n):
    num = int(input())
    
    # num까지 push
    while temp <= num:
        stack.append(temp)
        op.append('+')
        temp += 1
    
    # 스택 top이 원하는 숫자인지 확인
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(op))
else:
    print('NO')