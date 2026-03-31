import math

N = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
T, P =  map(int, input().split())

t_arr =[s, m, l, xl, xxl, xxxl]
t_result = 0
p_result1 = 0 
p_result2 = 0
# 티셔츠
for i in t_arr:
  t_result += math.ceil(i / T)

# 펜 
# 몫 
p_result1 += (N // P) 
# 나머지 
p_result2 += (N % P)

print(t_result)
print(p_result1, p_result2)