# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def maxDepth(cur) -> int:
            deep = 1
            for x in cur:
                if x.isInteger() is True:
                    continue
                deep = max(deep, 1 + maxDepth(x.getList()))
            return deep
        
        deep = maxDepth(nestedList)
        
        res = 0
        def dfs(cur, depth):
            nonlocal res, deep
            for x in cur:
                if x.isInteger() is True:
                    res += (deep - depth + 1) * x.getInteger()
                else:
                    dfs(x.getList(), depth + 1)
        dfs(nestedList, 1)
        return res
