class Solution:
    def earliestFinishTime(self, land_start_time: List[int], land_duration: List[int], water_start_time: List[int], water_duration: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: greedy

        result = float('inf')

        # land -> water
        land_earliest_end = float('inf')
        for i in range(len(land_start_time)):
            current_end_time = land_start_time[i] + land_duration[i]
            land_earliest_end = min(land_earliest_end, current_end_time)
        
        for i in range(len(water_start_time)):
            start_time = max(water_start_time[i], land_earliest_end)
            result = min(result, start_time + water_duration[i])
        
        # water -> land
        water_earliest_end = float('inf')
        for i in range(len(water_start_time)):
            current_end_time = water_start_time[i] + water_duration[i]
            water_earliest_end = min(water_earliest_end, current_end_time)

        for i in range(len(land_start_time)):
            start_time = max(water_earliest_end, land_start_time[i])
            result = min(result, start_time + land_duration[i])

        return result