class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        for row in range(rows):
            for column in range(len(words[row])):
                if column >= rows or row >= len(words[column]) or words[row][column] != words[column][row]:
                    return False
        return True