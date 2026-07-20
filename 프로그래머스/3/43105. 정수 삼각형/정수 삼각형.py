def solution(triangle):
    answer = 0
    #f[n][m] = min(f[n-1][m] + triangle[n][m], f[n-1][m+1] + triangle[n][m])
    route = [[0] * len(row) for row in triangle]
    route[0][0] = triangle[0][0]
    level = len(triangle)
    for n in range(1,level):
        for m in range(0,n+1):
            #삼각형의 양 끝 예외 처리
            if(m == 0):
                route[n][m] = route[n-1][m] + triangle[n][m]
            elif(m == n):
                route[n][m] = route[n-1][m-1] + triangle[n][m]
            else:
                route[n][m] = max(route[n-1][m-1],route[n-1][m]) + triangle[n][m]
    return max(route[-1])