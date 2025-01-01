import sys
input = sys.stdin.readline

n = int(input())

"""
n = 5 

n = 1 승자 : 상근
n = 2 승자 : 창영
"""


if n%2 == 0 :
  print("CY")
else :
  print("SK")