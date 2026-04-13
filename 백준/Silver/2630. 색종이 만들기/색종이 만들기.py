n = int(input())

m = []

for _ in range(n):
  l = list(map(int, input().split()))
  m.append(l)

blue = 0   #1
white = 0  #0

def v(row, col, size):
  global blue, white      
  current = m[row][col]
  for r in range(row, row + size):
    for c in range(col, col + size):
      if m[r][c] != current:
       half = size // 2
       v(row, col, half)
       v(row, col + half, half)
       v(row + half, col, half)
       v(row + half, col + half, half)
       return
  
  if current == 0:
    white +=1 
  else:
    blue += 1 

v(0,0,n)
print(white)
print(blue)
