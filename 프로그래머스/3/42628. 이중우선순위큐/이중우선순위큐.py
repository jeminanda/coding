class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class Heap:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if not self.root:
            self.root = Node(value)
            return
        curr = self.root
        while True:
            if(curr.value == value):
                return
            elif(curr.value > value):#현재 노드보다 추가할 값이 작을때
                if(curr.left is None):#현재 노드의 왼쪽 자식이 비어있으면 노드 생성 후 추가
                    curr.left = Node(value)
                    return
                curr = curr.left#아니면 왼쪽으로 계속 탐색
            elif(curr.value < value):
                if(curr.right is None):
                    curr.right = Node(value)
                    return
                curr = curr.right
    def pop_left(self):
        if not self.root:
            return None
        parent = None
        curr = self.root
        #노드의 가장 왼쪽으로 이동
        while curr.left:
            parent  = curr
            curr = curr.left
        #삭제한 노드의 오른쪽 자식을 부모의 왼쪽과 연결
        if parent:
            parent.left = curr.right
        else:
            self.root = curr.right
        return curr.value
    def pop_right(self):
        if not self.root:
            return None
        parent = None
        curr = self.root
        #노드의 가장 오른쪽으로 이동
        while curr.right:
            parent  = curr
            curr = curr.right
        if parent:
            parent.right = curr.left
        else:
            self.root = curr.left
        return curr.value
    
def solution(operations):
    dpq = Heap()
    for operation in operations:
        command,value = operation.split()   #문자열을 띄어쓰기 기준으로 받아옴
        value = int(value)
        if(command == 'I'): #첫 문자가 I일떄
            dpq.insert(value)
        elif(command == 'D'):#첫 문자가 D일때
            if(value == 1):
                dpq.pop_right()
            elif(value == -1):
                dpq.pop_left()
    if not dpq.root:
        return [0, 0]
    else:
        # 남아있는 최댓값과 최솟값 조회
        max_val = dpq.pop_right()
        # pop_max 후 큐가 비어버렸을 수도 있으므로 안전하게 pop_min 시도
        min_val = dpq.pop_left()
        if min_val is None:
            min_val = max_val
        return [max_val, min_val]