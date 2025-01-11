"""
- 문제
어떠한 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다.
당신은 어떤 자연수 N에 대해서 
이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 
사용하는 자연수는 N 이하여야 한다.

EX) 
15를 나타내는 방법 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 
10을 나타내는 방법 10, 1+2+3+4 2가지

N을 입력받아 가지수를 출력하는 프로그램을 작성

- 입력
  첫줄에 정수 N

- 출력
  입력된 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 출력.

- 예제 입력
  15

- 예제 출력
  4
- 문제 분석
  자연수 N을 나타내는 총 가지수를 구하는 문제 
** SUDO CODE **
  자연수 N을 연속된 자연수의 합으로 나타낼 것 
  내일 다시 보자

"""

import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = 1 

sum = 1 # 1 <= N
cnt = 0

while end < n+1: # 마지막 index가 n+1보다 작을 때까지 while 반복 
  if sum == n: # sum == n
    cnt += 1
    end += 1
    sum += end
    # print("sum == n",sum)
  
  elif sum < n : 
    end += 1
    sum += end
    # print("sum < n",sum)
  
  else : 
    sum -= start
    start += 1
    # print("sum > n",sum)

print(cnt)
