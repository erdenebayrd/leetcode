class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        """
        2 important things
            1. if current value (nums[i]) can go to any index at its right side when the right side value is smaller than nums[i]
            2. if current value is smaller than any element it's left side also can go directly
        
        meaning
        if we have prefix max and suffix min

        until index "i"
            if prefixMax[i] > suffixMin[i + 1]
                i'th index can join i + 1'th component (same component as i + 1 in)
            otherwise prefixMax <= suffixMin[i + 1]
                new component will begin
        after determining components for all index we can find max element of each component and each element of that component can reach the max value
        """
        # time: O(N)
        # space: O(N)
        # method: prefix + suffix + observations
        n = len(nums)
        prefixMax = [0] * n
        suffixMin = [0] * n
        prefixMax[0] = nums[0]
        suffixMin[n - 1] = nums[n - 1]
        for i in range(1, n):
            prefixMax[i] = max(nums[i], prefixMax[i - 1])
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])
        components = [0] * n
        components[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if prefixMax[i] > suffixMin[i + 1]:
                components[i] = components[i + 1]
            else:
                components[i] = components[i + 1] + 1
        maxValueByComponents = {}
        for i in range(n):
            component = components[i]
            if component not in maxValueByComponents:
                maxValueByComponents[component] = nums[i]
            maxValueByComponents[component] = max(nums[i], maxValueByComponents[component])
        result = [0] * n
        for i in range(n):
            component = components[i]
            value = maxValueByComponents[component]
            result[i] = value
        return result