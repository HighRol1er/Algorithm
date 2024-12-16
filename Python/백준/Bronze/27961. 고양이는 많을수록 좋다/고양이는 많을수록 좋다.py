"""

- 문제
  마법소녀 미도카는 고양이 N마리를 키우기로 결심
  한 번의 행동에서 2가지 마법 중 하나를 선택하여 사용 
  처음에는 미도카의 집에 고양이 존재 X 
  1. 생성 마법 : 고양이 한마리 집에 생성 
  2. 복제 마법 : 집에 있는 고양이 일부 또는 전부를 대상으로 하여 복제 
  즉, 현재 집에 고양이 k마리가 존재한다면, 0마리 이상 K마리 이하의 고양이를 집에 추가 가능 

  최소의 행동 횟수로 집에 정확히 N마리의 고양이가 있도록 만들고 싶다. 
- 입력
  첫 줄에 목표 고양이 수 N
- 출력
  마법을 최소 몇번 써야하는지 
- 예제 입력

- 예제 출력

- 문제 분석

** SUDO CODE **
"""

import sys
input = sys.stdin.readline

target = int(input())

magic = 0
cat = 0
# 0 => 1 => 2 => 4 => 6

while cat < target: 

  if cat == 0 or cat == 1:
    magic += 1 
    cat += 1
  elif cat > 1 :
    magic += 1
    cat *= 2

print(magic)

  
