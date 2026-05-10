class Solution:
    def trap(self, height: List[int]) -> int:
        """
        height = [4, 2, 0, 3, 2, 5]
        calculate how much water trap on each bar (on the top of the bar)
        the amount of water trapped on top of i'th bar is calculated.
        We need few variables
            1. maximum height of left side bars of i'th bar
            2. maximum height of right side bars of i'th bar
            3. minimum of [1] and [2], lets call it fence height
            4. the amount of water trapped on i'th bar is diff between [3] and current height (height[i]), more formally, [3] - height[i] is the amount of water
        so we can increase result by [4]
        """
        # # time: O(N)
        # # space: O(N) for storing maximum height of left and right bars
        # # method: kinda math

        # n = len(height)
        # leftMaxBar = height[0]
        # rightMaxBar = [0] * n
        # rightMaxBar[n - 1] = height[n - 1]
        # for index in range(n - 2, -1, -1):
        #     rightMaxBar[index] = max(rightMaxBar[index + 1], height[index])
        
        # result = 0
        # for index in range(1, n - 1):
        #     fence = min(rightMaxBar[index + 1], leftMaxBar)
        #     if fence - height[index] > 0:
        #         result += fence - height[index]
        #     leftMaxBar = max(leftMaxBar, height[index])
        # return result

        # ----------------------------------------- O(1) space, 2 pointers method -----------------------------------------

        """
        in prev approach, we calculate left max, right max heights.
        and get MINIMUM of left and right max
        since we only get minimum of left and right max, 
        we don't need to calculate all left and right max
        starting from left end which is 0
        starting from right end which is n - 1
        left pointer = 0
        right pointer = n - 1
        so if left pointer value is greater than right pointer value, 
        meaning, we would choose max right value as a minimum one. Even though there is some higher values in left of current "i". that doesn't matter since right max is lower than current left max
        thats the core idea.
        Why we need to move right pointer into left by 1 (not left pointer into right by 1)??
        we already calculated current i'th water that would be trapped at "i". we no longer keep right pointer at "i"
        """
        # time: O(N)
        # space: O(1)
        # method: 2 pointers

        """
        left.                          V
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        right                       ^

        leftMax = 2
        rightMax = 3
        result = 0 + 1 + 1 + 1 + 2 + 1
        """
        # n = len(height)
        # left, right = 0, n - 1
        # leftMax, rightMax = 0, 0
        # result = 0
        # while left <= right:
        #     if leftMax < rightMax:
        #         if leftMax - height[left] > 0:
        #             result += leftMax - height[left]
        #         leftMax = max(leftMax, height[left])
        #         left += 1
        #     else: # leftMax <= rightMax
        #         if rightMax - height[right] > 0:
        #             result += rightMax - height[right]
        #         rightMax = max(rightMax, height[right])
        #         right -= 1
        # return result
#------------------------------------------------------------------------------------------------------------------------------
        # time: O(N)
        # space: O(1)
        # method: 2 pointers
        n = len(height)
        result = 0
        leftMax, rightMax = height[0], height[n - 1]
        leftIndex, rightIndex = 0, n - 1
        while leftIndex <= rightIndex:
            if leftMax <= rightMax:
                if leftMax - height[leftIndex] > 0:
                    result += leftMax - height[leftIndex]
                leftMax = max(leftMax, height[leftIndex])
                leftIndex += 1
            else: # leftMax > rightMax
                if rightMax - height[rightIndex] > 0:
                    result += rightMax - height[rightIndex]
                rightMax = max(rightMax, height[rightIndex])
                rightIndex -= 1
        return result