n = int(input())
t = list(map(int, input().split()))
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    ans = t[:]
    ans[p-1] = x
    print(sum(ans))