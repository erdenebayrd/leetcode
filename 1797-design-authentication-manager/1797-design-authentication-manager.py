class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.nodes = {} # by key
    
    def append(self, key, value) -> None:
        node = Node(key=key, value=value)
        endNode = self.tail.prev
        endNode.next = node
        node.prev = endNode
        node.next = self.tail
        self.tail.prev = node
        self.nodes[key] = node
        self.size += 1
    
    def remove(self, key) -> None:
        if key not in self.nodes:
            return
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        del self.nodes[key]
        self.size -= 1

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.auths = LinkedList()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auths.append(key=tokenId, value=currentTime + self.ttl)

    def renew(self, tokenId: str, currentTime: int) -> None:
        while self.auths.head.next.key is not None and self.auths.head.next.value <= currentTime:
            self.auths.remove(self.auths.head.next.key)
        if tokenId not in self.auths.nodes:
            return
        node = self.auths.nodes[tokenId]
        self.auths.remove(node.key)
        node.value = currentTime + self.ttl
        self.auths.append(node.key, node.value)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.auths.head.next.key is not None and self.auths.head.next.value <= currentTime:
            self.auths.remove(self.auths.head.next.key)
        return self.auths.size

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)