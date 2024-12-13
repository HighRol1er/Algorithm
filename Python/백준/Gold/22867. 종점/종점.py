"""
- 문제
  주행을 마친 버스들이 종점에 들어온다. 
  종점에 들어온 버스는 버스를 정비하기 위한 자리에 들어간다. 
  즉, 종점에 버스 4대가 있다면 버스를 정비할 수있는 공간이 최소 4개 이상 필요 

  만약 같은 시각에 종점에 들어오는 버스 A와 종점에서 출발하는 버스B가 있을 경우 
  버스 B가 먼저 종점에서 출발하고 그 다음으로 버스 A가 들어온다. 
  
  버스의 시간표가 매일 동일하며 종점에 들어오는 시각과 나가는 시각이 매일 동일 

  이번에 버스 시간표가 변경이 되어 버스를 정비하는 공간이 최소 몇 개 이상 필요한지
  다시 계산을 해야한다. 

- 입력
  첫 번째 줄에는 종점에 들어오는 버스들의 개수 N
  두번째 줄 부턴 N + 1번째 줄까지 각 버스가 종점에 들어오는 시각과 종점에서 나가는 시간이 
  주어진다. 
  한 버스의 나가는 시각은 들어오는 시각보다 늦다. 

  주어진 시각의 형식은 다음과 같다. HH:MM:SS:sss 
- 출력
  버스 정비를 위한 공간이 최소 몇개 이상 필요한지 출력 

- 예제 입력

- 예제 출력

- 문제 분석

** SUDO CODE **
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
buses = []
for _ in range(N):
    in_time, out_time = input().split()
    # 시각, 분, 초, 밀리초를 계산해서 하나의 숫자로 해준다.
    in_time_final = int(in_time[9:]) + int(in_time[6:8]) * 1000 + int(in_time[3:5]) * 100000 + int(
        in_time[:2]) * 10000000
    out_time_final = int(out_time[9:]) + int(out_time[6:8]) * 1000 + int(out_time[3:5]) * 100000 + int(
        out_time[:2]) * 10000000
    buses.append((in_time_final, out_time_final))

# 출발 시각 이른 것부터 정렬
buses.sort()

Q = []
heapq.heappush(Q, (buses[0][1], buses[0][0]))  # 나가는 시각, 들어오는 시각
bus_one_time = 1

for i in range(1, N):  # 하나씩 쭉 보기
    fast_out = heapq.heappop(Q)  # 가장 빨리 나가는 버스
    if buses[i][0] < fast_out[0]:  # 가장 빨리 나가는 버스가 나가는 시각보다, 이번에 들어오는 버스가 더 빨리 들어오면
        bus_one_time += 1  # 종점에 같이 있어야 하니까 하나 더함
        heapq.heappush(Q, fast_out)  # 가장 빨리 나가는 버스가.. 안 나갔으니까 더해줌
        heapq.heappush(Q, (buses[i][1], buses[i][0]))  # 이번 버스도 들어옴
    else:  # 가장 빨리 나가는 버스가, 이번에 들어오는 버스보다 빨리 나가면
        heapq.heappush(Q, (buses[i][1], buses[i][0]))  # 이번 버스 들어옴
print(bus_one_time)
