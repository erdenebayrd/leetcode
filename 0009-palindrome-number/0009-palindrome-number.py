class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x
    

# Spoj/CSMS Шулуун будах solution
from typing import List, Tuple
from collections import defaultdict

def paintEdge(edges: List[Tuple[int, int, str]]) -> List[int]:
    edges.insert(0, (0, int(1e9), 'w'))
    paintsDict = defaultdict(int)
    current = 1
    for start, end, color in edges:
        paintColor = current
        if color == 'b':
            paintColor = -current
        paintsDict[start] += paintColor
        paintsDict[end] -= paintColor
        current += 1
    
    paintsArray = []
    for key in paintsDict:
        value = paintsDict[key]
        paintsArray.append([key, value])
    paintsArray.sort()
    for i in range(1, len(paintsArray)):
        paintsArray[i][1] += paintsArray[i - 1][1]
    
    leftIndex = 0
    res = 0
    answer = [0, int(1e9)]
    for rightIndex in range(1, len(paintsArray)):
        distance = paintsArray[rightIndex][0] - paintsArray[leftIndex][0]
        if paintsArray[leftIndex][1] > 0 and paintsArray[rightIndex][1] < 0: # white -> black
            if res < distance:
                res = distance
                answer = [paintsArray[leftIndex][0], paintsArray[rightIndex][0]]
            leftIndex = rightIndex
        elif paintsArray[leftIndex][1] < 0 and paintsArray[rightIndex][1] > 0: # black -> white
            leftIndex = rightIndex
        elif paintsArray[leftIndex][1] > 0 and paintsArray[rightIndex][1] >= 0: # white -> white
            if res < distance:
                res = distance
                answer = [paintsArray[leftIndex][0], paintsArray[rightIndex][0]]
    # print(paintsArray)
    # print(res)
    # print(answer)
    return answer
    
# n = int(input())
# edges = []
# for _ in range(n):
#     parts = input().split()
#     edges.append((int(parts[0]), int(parts[1]), parts[2]))
# res = paintEdge(edges)
# print(res[0], res[1])