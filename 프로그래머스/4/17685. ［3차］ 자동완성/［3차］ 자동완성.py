class node:
    def __init__(self):
        #children을 담은 정보를 딕셔너리로 선언
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = node()
    #단어 삽입
    def insert(self, word):
        curr = self.root
        for char in word:   #문자 하나씩 탐색
            if(char not in curr.children):  #중복되는 부분이 아니라면 노드 생성후 children에 추가
                curr.children[char] = node()    
            curr = curr.children[char]      #다음 문자로 넘어감
            curr.count += 1
    #단어에 필요한 입력의 개수
    def get_typed_count(self,word):
        curr = self.root
        typed_length = 0

        for char in word:
            curr = curr.children[char]
            typed_length += 1
            if curr.count ==1:  #이 문자를 거쳐가는 단어가 1개밖에 안남았을때(자동완성 확정이 가능할 떄)
                break
        return typed_length
def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return sum(trie.get_typed_count(word) for word in words)