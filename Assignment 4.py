# Memoization (Top-Down DP)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation (Bottom-Up DP)

def fibonacci_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Main Program

n = int(input("Enter the value of n: "))

print("Fibonacci using Memoization:", fibonacci_memo(n))
print("Fibonacci using Tabulation :", fibonacci_tab(n))

"""
Output:
Enter the value of n: 345
Fibonacci using Memoization: 563963353180680437428706474693749258212475354428320807161115873039415970
Fibonacci using Tabulation : 563963353180680437428706474693749258212475354428320807161115873039415970
"""