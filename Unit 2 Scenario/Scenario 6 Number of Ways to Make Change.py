
def count_ways(coins, amount):

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = dp[i] + dp[i - coin]
    return dp[amount]

coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))
ways = count_ways(coins, amount)
print("Total possible combinations:", ways)

"""
Output
Enter coin denominations: 1 2 5
Enter target amount: 5
Total possible combinations: 4
"""