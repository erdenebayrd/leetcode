class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # time: O(n * 2 ^ n) n is the count of parenthesis in the given string
        # space: O(n)
        # method: brute force - bitmask

        pos = []
        chars = []
        for i in range(len(s)):
            if s[i] in ["(", ")"]:
                pos.append(i)
            else:
                chars.append(i)
        
        def is_valid(bitmask: int) -> bool:
            count_open = 0
            for i in range(bitmask.bit_length()):
                if (bitmask >> i) & 1:
                    if s[pos[i]] == "(":
                        count_open += 1
                    else:
                        if count_open == 0:
                            return False
                        count_open -= 1
            return count_open == 0
        
        n = len(pos)
        valids = []
        for i in range(1, 1 << n):
            if is_valid(i):
                valids.append(i)
        
        longest = 0
        for bitmask in valids:
            longest = max(longest, bitmask.bit_count())
        

        def build(bitmask: int) -> str:
            res = []
            cur = 0
            for i in range(bitmask.bit_length()):
                if (bitmask >> i) & 1:
                    while cur < len(chars) and chars[cur] < pos[i]:
                        res.append(s[chars[cur]])
                        cur += 1
                    res.append(s[pos[i]])
            for i in range(cur, len(chars)):
                res.append(s[chars[i]])

            return "".join(res)

        result = set()
        for bitmask in valids:
            if longest == bitmask.bit_count():
                result.add(build(bitmask))
        
        if not result:
            cur = []
            for i in chars:
                cur.append(s[i])
            result.add("".join(cur))

        return list(result)