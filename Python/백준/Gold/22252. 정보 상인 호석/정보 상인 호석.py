import sys, heapq
input = sys.stdin.readline

Q = int(input())
gorilla = {}
result = 0

for _ in range(Q):
    q = input().split()
    action = q[0]
    go_name = q[1]
    if action == '1':
        if go_name not in gorilla:
            gorilla[go_name] = []
        for x in q[3:]:
            heapq.heappush(gorilla[go_name], -int(x))
    else:
        b = q[2]
        if go_name not in gorilla:
            continue
        for _ in range(min(int(b), len(gorilla[go_name]))):
            result += -heapq.heappop(gorilla[go_name])
print(result)