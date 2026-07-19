import heapq
def solution(n, s, a, b, fares):
    INF = float('inf')
    #인접 리스트 형식으로 그래프 구축
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))  # 양방향 도로
    #다익스트라 알고리즘 함수 정의
    def dijkstra(start):
        #최단 거리 테이블을 모두 무한대로 초기화
        distance = [INF] * (n+1)
        #시작 노드로 가기 위한 최단 거리는 0으로 설정 후 큐에 삽입
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        
        while q:
            #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            #현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue
            #현재 노드와 연결된 다른 인접한 노드들을 확인
            for next_node, weight in graph[now]:
                cost = dist + weight
                #현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧은 경우
                if cost < distance[next_node]:
                    distance[next_node] = cost #최단 거리값 갱신
                    heapq.heappush(q,(cost,next_node))
        return distance
    dist_s = dijkstra(s)    #출발지 s로부터 모든 노드까지의 최단 거리
    dist_a = dijkstra(a)    #A의 목적지 a로부터 모든 노드까지의 최단 거리
    dist_b = dijkstra(b)    #B의 목적지 b로부터 모든 노드까지의 최단 거리
    answer = INF
    #모든 노드를 순회하며 s부터 i까지의 최단거리+ i부터 a까지의 최단거리 + i부터 b까지의 최단거리 갱신
    for i in range(1,n+1):
        cost = dist_s[i] + dist_a[i] + dist_b[i]
        answer = min(answer,cost)
    return answer