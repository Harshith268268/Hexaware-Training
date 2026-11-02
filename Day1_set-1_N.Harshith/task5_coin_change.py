def greedy_change(amount, coins):
    result = []
    for coin in sorted(coins, reverse=True):
        count, amount = divmod(amount, coin)
        result.extend([coin] * count)
    return result if amount == 0 else None

def dp_change(amount, coins):
    dp = [float("inf")] * (amount + 1)
    previous = [None] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and dp[value - coin] + 1 < dp[value]:
                dp[value] = dp[value - coin] + 1
                previous[value] = coin
    if dp[amount] == float("inf"):
        return None
    result = []
    while amount > 0:
        coin = previous[amount]
        result.append(coin)
        amount -= coin
    return result

amount = 6
denominations = [4, 3, 1]
greedy = greedy_change(amount, denominations)
optimal = dp_change(amount, denominations)

print("Refund amount:", amount)
print("Coin denominations:", denominations)
print("Greedy solution:", greedy, "| number of coins:", len(greedy))
print("Dynamic programming solution:", optimal, "| number of coins:", len(optimal))
print("Greedy gives 4+1+1 (3 coins), but optimal is 3+3 (2 coins).")
print("Complexity: Greedy O(k log k) including sorting; DP O(A*k) time and O(A) space.")
