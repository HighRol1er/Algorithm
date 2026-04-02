N = int(input())
score = list(map(int, input().split()))

M = max(score)
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

new_score = []

for i in score:
  new_score.append(i/M * 100)

total_score = 0
for i in new_score:
  total_score += i

print(total_score/N)