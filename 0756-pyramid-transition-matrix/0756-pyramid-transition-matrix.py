class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pattern = {}
        for s in allowed:
            if s[:2] not in pattern:
                pattern[s[:2]] = []
            pattern[s[:2]].append(s[2])
        
        @cache
        def solve(bottom: str) -> bool:
            if len(bottom) <= 1:
                return True
            row = ""
            top = []
            for i in range(1, len(bottom)):
                base = bottom[i-1:i+1]
                if base not in pattern:
                    return False
                top.append(pattern[base])
            
            words = [""]
            for row in top:
                newWords = []
                for ch in words:
                    for col in row:
                        newWords.append(ch + col)
                words = newWords
            # print(bottom, words)
            res = False
            for word in words:
                res |= solve(word)
            return res
        
        return solve(bottom)