class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def intersectArea(i: int, j: int) -> int:
            leftI, bottomI = bottomLeft[i]
            rightI, topI = topRight[i]
            leftJ, bottomJ = bottomLeft[j]
            rightJ, topJ = topRight[j]
            if rightI <= leftJ or rightJ <= leftI or topI <= bottomJ or topJ <= bottomI: # no intersection
                return 0
            width = 0
            if leftI <= leftJ and rightJ <= rightI: # i contains j by X axis
                width = rightJ - leftJ
            elif leftJ <= leftI and rightI <= rightJ: # j continas i by X axis
                width = rightI - leftI
            elif rightI <= rightJ and leftJ <= rightI: # i then j
                width = rightI - leftJ
            elif rightJ <= rightI and leftI <= rightJ: # j then i
                width = rightJ - leftI
            else:
                assert False
            height = 0
            if bottomI <= bottomJ and topJ <= topI: # i contains j by Y axis
                height = topJ - bottomJ
            elif bottomJ <= bottomI and topI <= topJ:# j contains i by Y axis
                height = topI - bottomI
            elif topI <= topJ and bottomJ <= topI: # i then j
                height = topI - bottomJ
            elif topJ <= topI and bottomI <= topJ: # j then i
                height = topJ - bottomI
            else:
                assert False
            # print(height, width, i, j)
            return min(height, width) ** 2

        n = len(bottomLeft)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, intersectArea(i, j))
        return res