N,K = map(int, input().split())

# 이항 계수? 

def factorial(x):
  result = 1
  for i in range(1, x+1):
    result *= i
  return result

print( factorial(N) // (factorial(K) * factorial(N-K)))

  
