def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지 (아무 동전도 쓰지 않음)
    
    for coin in money:
        for price in range(coin, n + 1):
            dp[price] = (dp[price] + dp[price - coin]) % 1_000_000_007
            
    return dp[n]