N,K = map(int, input().split())

# 이항 계수? -> 주어진 집합에서 순서에 상관없이 일정 개수의 원소를 선택하는 방법의 가짓수 
#  $n$개 중에서 $k$개를 뽑는 경우의 수"**인 **조합(Combination)**과 같은 개념

def factorial(x):
  result = 1
  for i in range(1, x+1):
    result *= i
  return result

print( factorial(N) // (factorial(K) * factorial(N-K)))