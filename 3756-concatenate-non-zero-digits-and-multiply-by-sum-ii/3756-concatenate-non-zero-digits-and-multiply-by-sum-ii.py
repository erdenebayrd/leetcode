class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # time: O(Q)
        # space: O(N)
        # method: Rabin-Karp rolling hash style
        mod = 1_000_000_007
        n = len(s)
        digits = []
        for ch in s:
            if ch != '0':
                digits.append(int(ch))
        
        m = len(digits)
        if m == 0:
            return [0] * len(queries)

        left, right = [0] * n, [0] * n
        current_index = 0
        for i in range(n):
            left[i] = current_index
            if current_index < m and int(s[i]) == digits[current_index]:
                current_index += 1
        
        current_index = m - 1
        for i in range(n - 1, -1, -1):
            right[i] = current_index
            if current_index >= 0 and int(s[i]) == digits[current_index]:
                current_index -= 1
        
        base = 10
        bases = [0] * m
        bases[0] = 1
        for i in range(1, m):
            bases[i] = (bases[i - 1] * base) % mod
        
        prefix = [0] * m
        prefix[0] = digits[0]
        for i in range(1, m):
            prefix[i] = (prefix[i - 1] * base + digits[i]) % mod
        
        def query(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == 0:
                return prefix[right]
            return (prefix[right] - prefix[left - 1] * bases[right - left + 1]) % mod
        
        psum = [0] * n
        psum[0] = int(s[0])
        for i in range(1, n):
            psum[i] = psum[i - 1] + int(s[i])
        
        def psum_query(left: int, right: int) -> int:
            if left == 0:
                return psum[right]
            return psum[right] - psum[left - 1]
        
        result = []
        for query_left, query_right in queries:
            digit_sum = psum_query(query_left, query_right)
            query_left = left[query_left]
            query_right = right[query_right]
            concat_number = query(query_left, query_right)
            result.append((concat_number * digit_sum) % mod)
        return result

