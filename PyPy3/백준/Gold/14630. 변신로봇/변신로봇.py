"""
- 문제
  변신을 하기 위해선 동전을 넣어야 한다. 
  로봇의 현재 상태에서 부품의 형태가 가까운 변신일수록 돈이 적게 들고 먼 형태일 수록 돈이 많이 드는 구조이다.
  부품의 형태는 숫자로 나타낼 수 있고, 로봇의 상태는 그 숫자들의 모임으로 나타낼 수 있다.
  변신의 필요한 돈은 각 부품들의 숫자 차이를 제곱한 것의 합

  Ex_) 로봇의 현재 상태가 123이고 다른 상태가 222라면 변신에 필요한 돈은  (1-2)^2 + (2-2)^2 + (3-2)^2 = 2

  승균이를 대신해 돈을 가장 적게 사용해 승균이가 원하는 변신 상태를만들어주자.

- 입력
  첫 줄에 변신로봇의 변신 상태의 개수 N
  둘째줄 : N줄에 걸쳐 각 변신 상태에 대한 부품의 형태가 숫자로 주어진다.
  부품의 형태의 길이는 100을 넘지 않는다.

  길이가 다른 부품의 형태는 존재 X , 부품의 형태는 0으로 시작할 수 있다.

  다음 줄에 현재 변신상태의 번호와 승균이가 원하는 변신 상태의 번호가 주어진다. 번호는 위에 입력받은 순서대로 1부터 번호가 매겨져 있다고 가정한다.

- 출력
  첫째 줄에 현재 변신 상태로 승균이가 원하는 변신 상태를 만드는 대에 필요한 돈의 최솟값을 출력한다.

- 예제 입력
  3
  11 < 노드 1
  33 < 노드 2
  55 < 노드 3
  1 3 < 출발 노드 , 도착 노드


- 예제 출력
  16

- 문제 분석

출발 노드 -> 도착 노드 까지 가는데 최소 비용, 간선의 비용은 (노드n, i자리 수 - i자리 수 ) ^ 2 

노드 1 -> 노드 2 : (1-3)^2 + (1-3)^2 = 8
노드 1 -> 노드 3 : (1-5)^2 + (1-5)^2 = 32
노드 2 -> 노드 3 : (3-5)^2 + (3-5)^2 = 8

최소 비용을 쓰기 위해선 노드 1 -> 노드 2 -> 노드 3
** SUDO CODE **
"""
import  heapq

def dijkstra(start):
  distance[start] = 0
  heap = []
  heapq.heappush(heap,[0, start])
  while heap :
    dist, now = heapq.heappop(heap) # dist: 현재 노드까지의 비용 now: 현재 처리중인 노드 번호 
    # print("current node", now)
    if distance[now] < dist :  # 이미 처리된 노드는 continue
      continue
    for i in range(1, n+1): # 모든 노드에 대해 탐색 시작
      if i == now: # 현재 노드와 동일한 노드는 continue
        continue
      cost = dist # 초기 비용은 현재까지의 비용 dist로 설정
      for j in range(len(robot_stat[i])): # 각 상태의 부품 데이터를 비교 
        cost += (robot_stat[i][j] - robot_stat[now][j]) ** 2 
      if cost < distance[i]: # 새로운 비용이 기존 비용보다 작다면 갱신 
        distance[i] = cost # 최단 거리 갱신
        # print(distance)
        heapq.heappush(heap, [cost, i]) # 갱신된 비용과 노드를 힙에 추가.


n = int(input())

robot_stat = [[]] # 첫 번째 빈 리스트 추가 why? 인덱스 1부터 시작하기 위함

for _ in range(n):
    status = input()  
    status_list = [int(x) for x in status]  # "11" -> [1, 1]
    
    # 변환된 리스트를 robot_stat에 추가합니다.
    robot_stat.append(status_list) 

# print(robot_stat) # [[], [1, 1], [3, 3], [5, 5]]

start, end = map(int, input().split())

INF = int(1e9)

distance = [INF for _ in range(n+1)] # 최단경로 알고리즘에서 사용하는 거리 초기화 작업,
"""
1e9 = 10^9 = 1,000,000,000
다익스트라 알고리즘에서는 이 값을 사용해 비교

distance[i]의 값이 INF라면 노드 i까지 아직 도달하지 못했다.라는 뜻

// 초기 값 설정
distance = [1000000000, 1000000000, 1000000000, 1000000000]
"""
dijkstra(start)

print(distance[end])



