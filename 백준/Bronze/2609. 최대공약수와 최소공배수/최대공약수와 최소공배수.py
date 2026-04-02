N,M = map(int, input().split())

def gcd(m,n):
  if m < n:
    m, n = n, m
  if n == 0:
    return m
  if m % n == 0:
    return n
  else:
    return gcd(n, m%n)

print(gcd(N,M))
print(N*M//gcd(N,M))