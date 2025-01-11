N = int(input())
start = 1
end = 1
sum = 1
count = 0

while start <= N :
    if sum == N:
        count += 1
        sum -= start
        start += 1
    elif sum < N:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1
print(count)