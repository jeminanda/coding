def solution(n):
    combination = [0]* (n+1)
    combination[0] = 1 #빈 괄호도 1가지 케이스로 취급
    for i in range(1,n+1):
        for j in range(i):
            combination[i] += combination[j] *combination[i-1-j]
    return combination[n]