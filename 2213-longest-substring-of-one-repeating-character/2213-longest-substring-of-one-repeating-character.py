class Node:
    def __init__(self) -> None:
        self.left = self.right = -1
        self.left_char = self.right_char = ""
        self.left_count = self.right_count = self.max = 0

class SegmentTree:
    def __init__(self, text: str) -> None:
        self.n = len(text)
        self.text = text
        self.st = [Node() for _ in range(self.n * 4)]
        self.__build(1, 0, self.n - 1)

    def __build(self, pointer: int, left: int, right: int) -> None:
        if left == right:
            self.st[pointer].left_char = self.st[pointer].right_char = self.text[right]
            self.st[pointer].left_count = self.st[pointer].right_count = self.st[pointer].max = 1
            self.st[pointer].left = left
            self.st[pointer].right = right
            return
        self.__build(2 * pointer, left, (left + right) // 2)
        self.__build(2 * pointer + 1, (left + right) // 2 + 1, right)
        self.__merge(pointer)

    def __merge(self, pointer: int) -> None:
        left_child = self.st[2 * pointer]
        right_child = self.st[2 * pointer + 1]
        current = self.st[pointer]
        
        current.left_char = left_child.left_char
        current.right_char = right_child.right_char
        current.left_count = left_child.left_count
        current.right_count = right_child.right_count
        current.left = left_child.left
        current.right = right_child.right
        current.max = max(left_child.max, right_child.max)

        if left_child.right_char == right_child.left_char:
            current.max = max(current.max, left_child.right_count + right_child.left_count)
            if left_child.max == left_child.right - left_child.left + 1: # left child is whole one char
                current.left_count = left_child.right_count + right_child.left_count
            if right_child.max == right_child.right - right_child.left + 1: # right child is whole on char
                current.right_count = left_child.right_count + right_child.left_count

    def update(self, index: int, ch: str) -> None:
        self.__update(1, 0, self.n - 1, index, ch)

    def __update(self, pointer: int, left: int, right: int, index: int, ch: str) -> None:
        if left > right or left > index or right < index:
            return
        if index == left == right:
            self.st[pointer].left_char = self.st[pointer].right_char = ch
            return
        self.__update(2 * pointer, left, (left + right) // 2, index, ch)
        self.__update(2 * pointer + 1, (left + right) // 2 + 1, right, index, ch)
        self.__merge(pointer)

class Solution:
    def longestRepeating(self, s: str, query_characters: str, query_indices: List[int]) -> List[int]:
        # time: O(N * log N)
        # space: O(N)
        # method: Segment Tree
        segment_tree = SegmentTree(s)
        result = []
        for i in range(len(query_characters)):
            ch = query_characters[i]
            index = query_indices[i]
            segment_tree.update(index, ch)
            result.append(segment_tree.st[1].max)
        return result