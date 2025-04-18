class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            # m.group(0) is the entire match, m.group(1) is its first digit
            s = re.sub(
                r"(.)\1*", lambda m: str(len(m.group(0))) + m.group(1), s
            )
        return s