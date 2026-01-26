class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        minimumLength = len(strs[0])
        for string in strs:
            minimumLength = min(minimumLength, len(string))
        
        isTerminated = False
        while index < minimumLength and isTerminated is False:
            for i in range(len(strs)):
                if strs[0][index] != strs[i][index]:
                    index -= 1
                    isTerminated = True
                    break
            index += 1
        if index < 0:
            return ""
        return strs[0][:index]