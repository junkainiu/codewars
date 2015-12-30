def count_change(money, coins):
    # your implementation here
    coins.sort()
    result = 0
    cache = [coins[0]]
    for i,coin in enumerate(coins):
        while sum(cache) < money:
            if sum(cache) == money:
                result += 1
            cache.append(coin)
