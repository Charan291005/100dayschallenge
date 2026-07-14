def countWays(n, start, x):

    dp = [0] * (n + 1)

    dp[start] = 1

    for rock in range(start + 1, n + 1):

        for jump in range(1, x + 2):

            prev = rock - jump

            if prev >= start:
                dp[rock] += dp[prev]

    return dp[n]


n = 6
start = 3
x = 2

print(countWays(n, start, x))