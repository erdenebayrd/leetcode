class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:        
        """
            tc: O(N)
            sc: O(1)
                       L           R
        index.     0.  1.  2.  3.  4.  5
        goes       0.  2.  4.  1   3.  5
        goes (index * 2) % (2 * n - 1)
                   0   2.  4.  1.  3.  5

        nums[i] -> nums[(2 * index) % (2 * n - 1)] -> ....
        
        goesIndex = (2 * index) % (2 * n - 1)
        nums[goesIndex] = nums[i]

        def go(index):
            nextIndex = (2 * index) % (2 * n - 1)
            nums[nextIndex] = nums[index]
        
        -1000 <= element <= 1000
        0 <= element <= 2000
        11 bit number
        00000000000
        00000000001
        00000000010
        00000000011
        00000000100
        .....
        11111111111
        

        delta+.    0.  1.  2.  4.  5.  0
        Input:    [2,  5,  1,  3,  4,  7] n = 3            
        Output:   [2,  3,  5,  4,  1,  7] 
        """

        bit = 10

        def go(index):
            nextIndex = (2 * index) % (2 * n - 1)
            original = nums[index] & ((1 << bit) - 1)
            nums[nextIndex] |= (original << bit)
        
        for index in range(1, len(nums) - 1):
            go(index)
        
        for index in range(1, len(nums) - 1):
            nums[index] = (nums[index] >> bit)
        
        return nums


    