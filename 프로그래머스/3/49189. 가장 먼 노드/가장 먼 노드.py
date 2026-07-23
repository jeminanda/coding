from collections import deque
def solution(n, edge):
    #edge로부터 그래프 정보 구성
    graph = [[] for _ in range(n+1)]
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    #distance 는 [-1]*n으로 초기화
    distance = [-1] * (n+1)
    distance[1] = 0 #시작지점의 거리는 0
    q = deque([1])      #1번 노드와 연결된 노드부터 bfs 시작
    while q:
        current = q.popleft()   #queue에서 탐색할 노드(최소거리의 노드부터)를 꺼냄
        for neighbor in graph[current]: #현재 노드와 연결된 노드들을 탐색
            if(distance[neighbor] == -1):   #만약 해당 노드를 아직 탐색하지 않았다면
                distance[neighbor] = distance[current] + 1  #거리값을 갱신하고
                q.append(neighbor)          #queue에 해당 노드를 탐색할 노드로 추가
    max_dist = max(distance)    #가장 먼거리를 찾기
    return distance.count(max_dist) #가장 먼 거리를 가진 노드의 개수를 반환