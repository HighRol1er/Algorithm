"""

- 문제
  다음 소스는 N번째 피보나치 수를 구하는 C++ 함수

  ```
  int fib(int n) {
    if (n == 0) {
      printf("0");
      return 0;
    } else if (n == 1) {
      printf("1");
      return 1;
    } else {
      return fib(n-1) + fib(n-2)
    }
  }
  ```

  fib(3)을 호출하면 다음과 같은 일이 일어난다.

  fib(3)은 fib(2)와 fib(1)을 호출한다.
  fib(2)는 fib(1)과 fib(0)을 호출한다.
  두번째 호출한 fib(1)은 1을 출력하고 1을 리턴한다.
  fibonacci(0)은 0을 출력하고, 0을 리턴한다.

  fib(2)는 fib(1)과 fib(0)의 결과를 얻고 1을 리턴한다.
  첫번째 호출한 fib(1)은 1을 출력하고 1을 리턴한다.
  fib(3)은 fib(2) 와 fib(1)의 결과를 얻고 2fibonacci(0)은 0을 출력하고, 0을 리턴한다.를 리턴한다.

  1은 2번 0은1번 출력된다.

  N이 주어졌을 때 fib(N)을 호출했을 때 , 0과 1이 각각 몇번 출력되는지 
  구하는 프로그램을 작성하시오

- 입력
  3
  0
  1
  3

- 출력
  1 0
  0 1
  1 2


- 문제 분석

** SUDO CODE **
피보나치 수열에서 구하는 시간 단축하는 유명한 방법은 dp
그리고 dp테이블을 한 번 구해 놓으면 테스트 케이스가 여러개 나오니까
다음 케이스에서도 재활용할 수도 있다.
"""

import sys
input = sys.stdin.readline

dp = [-1] * 41
zero_cnt = [0] * 41
one_cnt = [0] * 41

dp[0] = 0
dp[1] = 1

zero_cnt[0] = 1
one_cnt[1] = 1

def fibonacci(n):
    if dp[n] != -1:
        return

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
        zero_cnt[i] = zero_cnt[i - 2] + zero_cnt[i - 1]
        one_cnt[i] = one_cnt[i - 2] + one_cnt[i - 1]

t = int(input())

for _ in range(t):
  n = int(input())
  fibonacci(n)
  print(zero_cnt[n], one_cnt[n])