'''
카드가 한 장 남을 때까지 반복 
1. 제일 위에 있는 카드를 버린다. 
2. 제일 위에 있는 카드를 제일 아래로 옮긴다.
'''
from collections import deque

N = int(input())
cards = list(range(1, N + 1))

q = deque(cards)

flag = True
while len(q) != 1:
  if flag == True:
    q.popleft()
    flag = False
  else:
    temp = q.popleft()
    q.append(temp)
    flag = True

print(q[0])