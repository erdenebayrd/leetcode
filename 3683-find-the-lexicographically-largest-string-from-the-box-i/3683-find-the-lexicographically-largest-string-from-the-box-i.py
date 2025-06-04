class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        sz = len(word) - numFriends + 1
        arr = []
        for i in range(len(word)):
            arr.append(word[i : min(i + sz, len(word))])
        arr.sort()
        # print(arr)
        return arr[-1]