class Solution:
    def minSwaps(self, s: str) -> int:
        """
        we can count extra closing brackets from left to right
        and take maximum of extra closing brackets

        ))((
        in this example we can swap first and last brackets and the string becomes balanced
        extra closing brackets is 2 starting from left to right

        okay, now lets work on more complicated test case

        ))))))         (())     )))     (((((((((
        6 close.   balanced   3closed    9 opens

        maximum reach of extra closed would be 9 = (first 6 + 3 closed after the balanced)
        meaning
        this 9 closing brackets has to be swapped with opening brackets 
        but if we swap first closing bracket with open bracket which is located somewhere else
        () ))))
        2.  4 closing

        meaning after 1 swap the closing brackets decreased by 2
        since there is 9 closing brackets extra
        meaning 9 // 4 swaps are required
        since 9 is odd value we can do one more swap to make it balanced

        we can keep track of current extra closing brackets
        and take maximum of them

        divided by 2 + 1 if extra closing brackets is oddd
        this swaps are required at minimum
        """
        # time: O(N) N is the length of given string s
        # space: O(1)
        # method: observation

        extra_closing_brackets = 0
        max_extra_closing_brackets = 0
        for bracket in s:
            if bracket == ']':
                extra_closing_brackets += 1
            else: # opening bracket
                extra_closing_brackets -= 1
            max_extra_closing_brackets = max(max_extra_closing_brackets, extra_closing_brackets)
        
        swaps = max_extra_closing_brackets // 2 + max_extra_closing_brackets % 2
        return swaps