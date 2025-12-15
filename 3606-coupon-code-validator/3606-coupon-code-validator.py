class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        coupons = []
        for i in range(n):
            if isActive[i] is False or businessLine[i] not in categories or code[i] == "":
                continue
            flag = True
            for ch in code[i]:
                if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9' or ch == "_"):
                    flag = False
                    break
            if flag is True:
                coupons.append([businessLine[i], code[i]])
        return [code for _, code in sorted(coupons)]