class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        
        def build(left: int, right: int) -> str:
            if left >= right:
                return ""
            level = 0
            mountains = []
            while left < right:
                currentRight = left
                while currentRight <= right:
                    if s[currentRight] == '1':
                        level += 1
                    else:
                        level -= 1
                    if level == 0:
                        current = s[left] + build(left + 1, currentRight - 1) + s[currentRight]
                        mountains.append(current)
                        left = currentRight + 1
                    currentRight += 1
            mountains.sort(reverse = True)
            return "".join(mountains)
        
        result = build(0, len(s) - 1)
        return result