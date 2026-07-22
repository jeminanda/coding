from collections import deque
def solution(begin, target, words):
    if target not in words:     #타겟이 words 내에 없을 경우 0을 리턴
        return 0
    queue = deque([(begin, 0)]) #bfs를 구현하기 위해 queue 구조를 사용
    visited = set()             #중복을 방지하는 set 구조로 bfs의 visited를 구현
    while queue:                #return할떄까지 종료되지 않는 반복문
        current_word,steps = queue.popleft()    #queue에 처음 들어간 word,steps를 dequeue
        if(current_word == target):             #target 도달시 변환횟수 리턴
            return steps
        for word in words:          #words에 있는 모든 word 순회
            if word not in visited and sum(a != b for a,b in zip(current_word,word)) == 1: #아직 방문하지 않았고, 한글자만 다른경우
                visited.add(word)      #visited에 추가하고, queue에도 추가
                queue.append((word,steps+1))
    return steps
