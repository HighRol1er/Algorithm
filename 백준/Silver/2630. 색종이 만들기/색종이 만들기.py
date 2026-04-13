n = int(input())

matrix = []

for _ in range(n):
  l = list(map(int, input().split()))
  matrix.append(l)

blue = 0
white = 0 

def recursion(row, col, size):
  global blue,white
  current = matrix[row][col] # 0 or 1

  for r in range(row, row + size):
    for c in range(col, col + size):
      if matrix[r][c] != current:
        half = size // 2
        #I
        recursion(row, col, half)
        # II
        recursion(row + half, col, half)
        # III
        recursion(row, col + half, half)
        # IV 
        recursion(row+ half, col + half, half)
        return
      
  if current == 0:
    white +=1 
  else:
    blue += 1
  
recursion(0,0,n)
print(white)
print(blue)
