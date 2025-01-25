n = int(input())
arr = list(map(int, input().split()))

left = 0
ans = 0
count = {}

for right in range(n):
    count[arr[right]] = count.get(arr[right], 0) + 1

    while len(count) > 2:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)
