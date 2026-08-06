class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False
        self.fail_link = None
        self.output_link = None

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.root.fail_link = self.root
    
    def add_word(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_word = True
    
    def build_links(self) -> None: # only fail link, no need of output link
        queue = deque([self.root])
        while queue:
            parent_node = queue.popleft()
            for ch in parent_node.children:
                child = parent_node.children[ch]
                fail = parent_node.fail_link

                while ch not in fail.children and fail != self.root:
                    fail = fail.fail_link
                
                child.fail_link = self.root
                if ch in fail.children and fail.children[ch] != child:
                    child.fail_link = fail.children[ch]
                
                output_link = child.fail_link.output_link
                if child.fail_link.is_word:
                    output_link = child.fail_link
                child.output_link = output_link

                queue.append(child)

class StreamChecker:
    def __init__(self, words: List[str]):
        trie = Trie()
        for word in words:
            trie.add_word(word)
        trie.build_links()
        self.root = trie.root
        self.current_pointer = self.root

    def query(self, letter: str) -> bool:
        while letter not in self.current_pointer.children and self.current_pointer != self.root:
            self.current_pointer = self.current_pointer.fail_link
        if letter in self.current_pointer.children:
            self.current_pointer = self.current_pointer.children[letter]
        return self.current_pointer.is_word or self.current_pointer.output_link is not None

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)