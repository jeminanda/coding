from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        current_word,steps = queue.popleft()
        if(current_word == target):
            return steps
        for word in words:
            if word not in visited and sum(a != b for a,b in zip(current_word,word)) == 1:
                visited.add(word)
                queue.append((word,steps+1))
    return steps