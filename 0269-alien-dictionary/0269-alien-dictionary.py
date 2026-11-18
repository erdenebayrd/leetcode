class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # time: O(V * E) V is number of chars, E is length of words array
        # space: O(V)
        # method: Kahn algo cycle detection

        graph = {}
        color = {}
        for word in words:
            for ch in word:
                color[ch] = 0
                if ch not in graph:
                    graph[ch] = []
        
        def build_graph(left: int, right: int, index: int) -> bool:
            if left >= right:
                return True
            
            if index >= max([len(words[i]) for i in range(left, right + 1)]):
                return True

            prev = left
            for i in range(left + 1, right + 1):
                if index < len(words[i - 1]) and index >= len(words[i]):
                    return False
                if index >= len(words[i - 1]) or index >= len(words[i]):
                    continue

                if words[i - 1][index] != words[i][index]:
                    graph[words[i - 1][index]].append(words[i][index])
                    if not build_graph(prev, i - 1, index + 1):
                        return False
                    prev = i
            
            if not build_graph(prev, right, index + 1):
                return False
            
            return True

        n = len(words)
        if not build_graph(0, n - 1, 0):
            return ""

        

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