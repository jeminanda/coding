def solution(info, edges):
    answer =[0]
    tree = [[] for _ in range(len(info))]
    for i,j in edges:
        tree[i].append(j)
        
    sheep = 0
    wolf = 0
    index = 0
    def dfs(index,sheep,wolf,next_node):
        if(info[index] ==0):
            sheep += 1
        else:
            wolf += 1
        
        if(wolf >= sheep):
            return
        
        answer[0] = max(answer[0], sheep)
        new_next = next_node + tree[index]
        new_next.remove(index)
        
        for nxt in new_next:
            dfs(nxt, sheep, wolf, new_next)
    dfs(0,0,0,[0])
        
    return answer[0]