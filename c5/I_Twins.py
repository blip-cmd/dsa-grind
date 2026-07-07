n_coins = int(input())
coins = list(map(int, input().split()))

# we want biggest sum with least coins
coins.sort(reverse=True)
_sum = sum(coins)
half_sum = _sum / 2

current_sum 
for i, coin in enumerate(coins):
    current_sum += coin
    if current_sum > half_sum:
        print(i + 1)
        break
