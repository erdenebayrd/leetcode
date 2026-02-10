class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # time: O(N)
        # sapce: O(1)
        # method: 2 pointer
        def getIntersectionPair(firstPair, secondPair):
            start = max(firstPair[0], secondPair[0])
            end = min(firstPair[1], secondPair[1])
            if start <= end:
                return [start, end]
            return []

        firstPointer = 0
        secondPointer = 0
        result = []
        while firstPointer < len(firstList) and secondPointer < len(secondList):
            intersection = getIntersectionPair(firstList[firstPointer], secondList[secondPointer])
            if intersection:
                result.append(intersection)
            if firstList[firstPointer][1] < secondList[secondPointer][1]:
                firstPointer += 1
            else:
                secondPointer += 1
        return result