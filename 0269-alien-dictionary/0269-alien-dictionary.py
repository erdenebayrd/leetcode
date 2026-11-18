class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # time: O(V * E) V is number of chars, E is length of words array
        # space: O(V)
        # method: Kahn algo cycle detection

        n = len(words)
        graph = {}
        color = {}
        for word in words:
            for ch in word:
                color[ch] = 0
                graph[ch] = []
        
        for i in range(1, n):
            length = min(len(words[i]), len(words[i - 1]))
            if len(words[i - 1]) > len(words[i]) and words[i - 1][:length] == words[i][:length]:
                return ""

            for j in range(length):
                if words[i - 1][j] != words[i][j]:
                    graph[words[i - 1][j]].append(words[i][j])
                    break

        path = []
        def has_cycle(node: str) -> bool:
            if color[node] == 1:
                return True
            color[node] = 1 # visiting
            for neighbor in graph[node]:
                if color[neighbor] == 2:
                    continue
                if has_cycle(neighbor):
                    return True
            path.append(node)
            color[node] = 2 # done
            return False

        for node in graph:
            if color[node] == 0 and has_cycle(node):
                return ""
        
        return "".join(path[::-1])