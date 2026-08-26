class Solution:
    def countDistinct(self, s: str) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: Suffix Array LCP

        def bucket_sort(ranks: list, key: int) -> list:
            n = len(ranks)
            count = [0] * (n + 1)
            for i in range(n):
                count[ranks[i][key] + 1] += 1
            
            for i in range(1, n + 1):
                count[i] += count[i - 1]
            
            bucket = [0] * n
            for i in range(n - 1, -1, -1):
                count[ranks[i][key] + 1] -= 1
                bucket[count[ranks[i][key] + 1]] = ranks[i]
            return bucket

        def radix_sort(ranks: list) -> list:
            ranks = bucket_sort(ranks, 1)
            ranks = bucket_sort(ranks, 0)
            return ranks

        def build_sa(text: str) -> list:
            n = len(text)
            ranks = [(ord(text[i]), -1, i) for i in range(n)]
            ranks.sort()
            for bitmask in range(n.bit_length()):
                updated_ranks = [0] * n
                pos = [0] * n # ranks position by suffix index
                for i in range(1, n):
                    updated_ranks[i] = updated_ranks[i - 1]
                    if ranks[i - 1][0] != ranks[i][0] or ranks[i - 1][1] != ranks[i][1]:
                        updated_ranks[i] += 1
                    pos[ranks[i][2]] = i
                
                for i in range(n):
                    j = ranks[i][2] + (1 << bitmask)
                    rank = -1
                    if j < n:
                        rank = updated_ranks[pos[j]]
                    ranks[i] = (updated_ranks[i], rank, ranks[i][2])
                
                # ranks = sorted(ranks) # O(N log N)
                ranks = radix_sort(ranks) # TODO: implement radix sort O(N)
            return [i for _, _, i in ranks]

        def build_lcp(sa: list, text: str) -> list:
            n = len(sa)
            lcp = [0] * n
            pos = [0] * n
            for i in range(n):
                pos[sa[i]] = i
            
            prev_matched = 0
            for i in range(n):
                curr = pos[i]
                prev = curr - 1
                if prev == -1:
                    prev_matched = 0
                    continue

                matched = 0
                if prev_matched:
                    matched = prev_matched - 1
                
                while sa[curr] + matched < n and sa[prev] + matched < n and text[sa[curr] + matched] == text[sa[prev] + matched]:
                    matched += 1
                lcp[curr] = matched
                prev_matched = matched
            
            return lcp
        
        n = len(s)
        sa = build_sa(s)
        lcp = build_lcp(sa, s)

        # for i in range(n):
        #     print(lcp[i], sa[i], s[sa[i]:])

        result = 0
        for i in range(n):
            result += n - sa[i] - lcp[i]
        return result