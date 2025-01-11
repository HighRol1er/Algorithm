"""
- 문제
  인서, 준석, 정우, 진우, 영기 
  아래와 같은 계산법을 바탕으로 최종 일의 양을 계산해 가장 일이 바쁘지 않은 사람에게 일처리를 맡기기로 하였다.

  1. 5개의 일이 존재한다.
  2. 인서 ~ 영기 각자 1~5번의 번호를 부여 

  3. 행렬 A는 인서 ~ 영기가 예상한 1번째 일의 난이도, 5행2열의 값은 5번인 영기가 예상한 2번째 일의 난이도이다.

  4. 행렬 B는 인서 ~ 영기가 예상한 각 일의 처리시간을 각 행에 일의 순서대로 나열한 5x5 행열이다. 
  즉, x행 y열의 값은 x번 사람이 예쌍한 y번째 일의 처리시간이다.
  
  Ex) 
  2행 1열의 값은 2번인 준석이가 예상한 1번째 일의 처리시간, 5행 2열의 값은 5번인 영기가 예상한 2번째 일의 처리시간.

  5. x번 사람의 y번째의 일의 예상 일의 양은 아래와 같다.
  (문제 참고)

  6. 각자의 최종 일량은 1번째 일부터 5번째 일까지 그 사람의 예상 일량을 모두 합한 값이다.

  7. 최종 일량이 가장 작은 사람이 가장 일이 바쁘지 않은 사람이다.

  이 계산법으로 작동하는 프로그램을 구현하여 가장 일이 바쁘지 않은 사람을 구하여라.

- 입력
  5x5 행렬 A의 값 a1 ~ a25가 5줄에 걸쳐 순서대로 주어지며, 이후 5x5 행렬 B의 값 b1 ~ b25가 5줄에 걸쳐 순서대로 주어진다.
  단, ai는 1보다 크거나 같고 1000보다 작거나 같은 정수이며, bi는 1보다 크거나 같고 100보다 작거나 같은 정수이다.


- 출력
가장 일이 바쁘지 않은 사람의 이름(Inseo, Junsuk, Jungwoo, Jinwoo, Youngki)을 출력한다.
만약, 가장 일이 바쁘지 않은 사람이 둘 이상일 경우 Youngki, Jinwoo, Jungwoo, Junsuk, Inseo 순서로 가장 앞서는 사람의 이름을 출력

- 예제 입력
  A행렬
  
  40 50 20 70 10
  80 20 20 20 50
  50 20 10 30 60  
  90 10 30 20 40
  10 30 60 10 70
  
  B행렬
  
  10 30 20 20 20
  50 10 10 10 10
  30 10 10 10 40   
  60 10 10 10 10
  10 20 40 10 10

- 예제 출력 
  Jungwoo

- 문제 분석

** SUDO CODE **
"""

import sys
input = sys.stdin.readline

A = []

B = []

for _ in range(5):
  row = list(map(int, input().split()))
  A.append(row)

for _ in range(5):
  row = list(map(int, input().split()))
  B.append(row)

person = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
total = [0,0,0,0,0]

for x in range(5): 
  for y in range(5):
    expect_work = sum(A[x][i] * B[i][y] for i in range(5))
    total[x] +=  expect_work


# print(total) # [18400, 18300, 16200, 18500, 16200]

# min_index = 

# a = [18400, 18300, 16200, 18500, 16200]

min_time = min(total)
min_index = ([i for i, value in enumerate(total) if value == min_time])

# print(min_index)

if len(min_index) > 1:
  print(person[min_index[-1]])
else :
  print(person[min_index[0]])
