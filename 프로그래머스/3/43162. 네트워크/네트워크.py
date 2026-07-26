from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        #아직 방문하지 않은 컴퓨터를 발견하면 새 네트워크 시작
        if not visited[i]:
            answer+=1
            queue = deque([i])
            visited[i] = True
        while queue:
            curr = queue.popleft()
            for next_node in range(n):
                #아직 방문 안했고, 현재 노드랑 연결된 노드를 큐에 추가
                if computers[curr][next_node] == 1 and not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)     
    return answer