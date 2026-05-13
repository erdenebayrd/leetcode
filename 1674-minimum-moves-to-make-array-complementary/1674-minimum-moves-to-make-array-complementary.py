class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
            first observation is since we can change any index value to [1 -> limit] inclusive
            the complementary value can be [2 -> 2 * limit]
            
            we need to think in below way

            which intervals of complementary value requires how many changes on each pair (a[i], a[n - 1 - i])

            lets call complementary value as "c_value"
                * 2 <= "c_value" <= 2 * limit

            lets call a[i], a[n - 1 - i] as "min_value[i]", "max_value[i]" min value is minimum of them, max is maximum of them

            2 changes required
                * 2 <= "c_value" <= min_value[i]" we need 2 changes because even we change "max_value[i]" to 1 c_value has to be "min_value[i]" + 1 but that's not the case
                * "max_value[i]" + limit + 1 <= "c_value" <= 2 * limit
            
            1 change required
                * "min_value[i] + 1" <= "c_value" <= "max_value[i]" + limit
            
            0 change required
                * "min_value[i]" + "max_value[i]" == "c_value"
            
            * the condition 0 change required always inside of the interval 1 change required

            meaning, we can reduce intervals of "c_value"
            and sum up all changes of each pairs as delta array
        """
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        for i in range(n // 2):
            min_value = min(nums[i], nums[n - 1 - i])
            max_value = max(nums[i], nums[n - 1 - i])
            diff[2] += 2
            diff[min_value + 1] -= 1
            diff[min_value + max_value] -= 1
            diff[min_value + max_value + 1] += 1
            diff[max_value + limit + 1] += 1
        
        for i in range(3, 2 * limit + 1):
            diff[i] += diff[i - 1]
        
        return min(diff[2:2*limit + 1])