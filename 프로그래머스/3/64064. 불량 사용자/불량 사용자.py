def is_match(user, ban):
    if len(user) != len(ban):
        return False
    for u, b in zip(user, ban):
        if b != '*' and u != b:
            return False
    return True
from collections import deque
def solution(user_id, banned_id):
    case = set()
    queue = deque([(0,[])])
    while queue:
        index,visited = queue.popleft()
        if(index == len(banned_id)):
            banned_set = tuple(sorted(visited)) #visited의 중복을 막기위해 정렬하여 tuple로 만듬
            case.add(banned_set)    #banned_set를 set에 추가
            continue
        for _id in user_id:#banned_id에서 visited를 제외하고 가능한 경우의수를 찾음
            if(_id not in visited and is_match(_id,banned_id[index])):    #경우에 수에 맞으면 해당 id를 visited에 추가하고 다음 인덱스를 큐에 추가
                queue.append([index+1,visited + [_id]])
    return len(case)
    #1.BFS
    #banned_list[0]에 있는것부터 가능한 경우의 수 중 하나를 제거하고 순회할 banned_id의 인덱스와 visited를 queue에 추가
    #최종 목록은 중복을 막기위해 set를 인자로가지는 list로 구현
    