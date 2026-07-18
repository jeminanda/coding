import sys
# 파이썬의 기본 재귀 깊이 제한(1,000)을 늘려 컴파일 에러(Runtime Error)를 방지합니다.
sys.setrecursionlimit(2000)
# 전위 순회 (Root -> Left -> Right)
def preorder(node, result):
    if node is None:
        return
    result.append(node.id)       # 1. 현재 노드(루트) 번호 기록
    preorder(node.left, result)  # 2. 왼쪽 서브트리 방문
    preorder(node.right, result) # 3. 오른쪽 서브트리 방문

# 후위 순회 (Left -> Right -> Root)
def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)  # 1. 왼쪽 서브트리 방문
    postorder(node.right, result) # 2. 오른쪽 서브트리 방문
    result.append(node.id)        # 3. 현재 노드(루트) 번호 기록
def insert_node(parent, child):
    # 자식 노드의 x가 부모 노드의 x보다 작으면 왼쪽 서브트리로
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insert_node(parent.left, child)
    # 자식 노드의 x가 부모 노드의 x보다 크면 오른쪽 서브트리로
        else:
            if parent.right is None:
                parent.right = child
            else:
                insert_node(parent.right, child)
#BST를 구성하는 Node 클래스 정의
class Node:
    def __init__(self, x, y, node_id):
        self.x = x
        self.y = y
        self.id = node_id
        self.left = None
        self.right = None
#nodeinfo를 받아 root부터 2진트리 구성
def makeBST(nodeinfo):
    #BST를 만들때 초기 인덱스 정보를 포함시켜 만들기 위한 리스트
    nodes = [[v[0], v[1], i+1]for i,v in enumerate(nodeinfo)]
    #리스트를 y기준 내림, x기준 오름차순으로 정렬
    nodes.sort(key = lambda x:(-x[1],x[0]))
    #루트 노드는 정렬된 리스트의 첫번쨰 원소
    root = Node(nodes[0][0], nodes[0][1], nodes[0][2])
    # 두번째 노드부터 루트 노드 밑에 삽입
    for i in range(1,len(nodes)):
        child = Node(nodes[i][0], nodes[i][1], nodes[i][2])
        insert_node(root, child)
    return root

def solution(nodeinfo):
    # 1. 트리 구성 (기존에 작성하신 makeBST 활용)
    root = makeBST(nodeinfo)
    
    # 2. 순회 결과를 담을 빈 리스트 준비
    pre_result = []
    post_result = []
    
    # 3. 루트 노드부터 순회 시작
    preorder(root, pre_result)
    postorder(root, post_result)
    
    # 4. [전위 순회 결과, 후위 순회 결과] 형태로 반환
    return [pre_result, post_result]