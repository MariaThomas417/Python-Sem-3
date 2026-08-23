
def house_robber(houses):
    n = len(houses)
    if n == 0:
        return 0

    if n == 1:
        return houses[0]

    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])

    return dp[n - 1]


houses = list(map(int, input("Enter the amount in each house: ").split()))
maximum_amount = house_robber(houses)
print("Maximum amount that can be collected:", maximum_amount)

"""
Output 
Enter the amount in each house: 100 50 200 30 100
Maximum amount that can be collected: 400
"""