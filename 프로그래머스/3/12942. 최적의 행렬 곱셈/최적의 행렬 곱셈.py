def solution(matrix_sizes):
    n = len(matrix_sizes)
    # dp[i][j]: i번째부터 j번째 행렬까지 곱하는 최소 연산 횟수
    dp = [[0] * n for _ in range(n)]
    
    # length: 곱할 행렬의 개수 (2개부터 n개까지)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # i와 j 사이의 분할 지점 k
            for k in range(i, j):
                # dp[i][k] + dp[k+1][j] + (i의 행 * k의 열 * j의 열)
                cost = dp[i][k] + dp[k+1][j] + (matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    return dp[0][n-1]