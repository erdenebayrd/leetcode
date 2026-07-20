class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # time: O(len(s) + len(a) + len(b))
        # space: O(len(s) + len(a) + len(b))
        # method: Z algo
        def z_function(pattern: str, text: str) -> list:
            original_text = text
            text = pattern + text
            n = len(text)
            z_values = [0] * n
            z_values[0] = n
            left = right = -1
            for i in range(1, n):
                if i <= right:
                    z_values[i] = min(z_values[i - left], right - i + 1)
                while i + z_values[i] < n and text[z_values[i]] == text[i + z_values[i]]:
                    z_values[i] += 1
                if i + z_values[i] - 1 > right:
                    left = i
                    right = i + z_values[i] - 1
            is_found = [False] * len(original_text)
            for i in range(len(pattern), n):
                if z_values[i] >= len(pattern):
                    index = i - len(pattern)
                    is_found[index] = True
            return is_found
        
        a_found = z_function(a, s)
        b_found = z_function(b, s)
        n = len(s)

        indices = []
        left = right = count = 0
        for i in range(n):
            if not a_found[i]:
                continue
            while i - k > left:
                if b_found[left]:
                    count -= 1
                left += 1
            while right < n and right <= i + k:
                if b_found[right]:
                    count += 1
                right += 1
            if count:
                indices.append(i)

        return indices