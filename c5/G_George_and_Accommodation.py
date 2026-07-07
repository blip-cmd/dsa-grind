n = int(input())

result = 0
for _ in range(n):
    a, b = input().split()
    if int(b) - int(a) >= 2:
        result += 1

print(result)