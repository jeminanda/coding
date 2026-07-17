#시간 T가 주어졌을때 해당 시간안에 해결 가능한지 판단하는 함수
def is_possible(a, b, g, s, w, t, T):
    total_gold = 0
    total_silver = 0
    total_weight = 0

    for i in range(0,len(g)):
        # T 시간 동안 왕복 및 마지막 편도 횟수 계산
        truck_move = (T // (2 * t[i])) + (T // t[i]) % 2
        max_take = w[i] * truck_move

        # 1. 이 도시에서 최대로 가져올 수 있는 금의 양
        total_gold += min(g[i], max_take)
        
        # 2. 이 도시에서 최대로 가져올 수 있는 은의 양
        total_silver += min(s[i], max_take)
        
        # 3. 이 도시에서 최대로 가져올 수 있는 (금+은) 총 광물의 양
        total_weight += min(g[i] + s[i], max_take)

    # 3가지 조건을 모두 충족하면 T 시간 내에 운반 가능
    return total_gold >= a and total_silver >= b and total_weight >= (a + b)
    
def solution(a, b, g, s, w, t):
    #이진 탐색, T는 적당히 큰 수인 10 ** 15로 시작
    answer = -1
    start = 1
    end = 10 ** 15
    while(start <= end):
        T = (start + end)//2
        if(is_possible(a,b,g,s,w,t,T)):
            answer = T
            end = T - 1
        else:
            start = T + 1
    return answer
    
        
        
        
    