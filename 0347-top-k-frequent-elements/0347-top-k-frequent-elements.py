import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time: average: O(N) worst O(N ^ 2)
        # space: O(N)
        # method: like a quicksort
        if k <= 0:
            return []
        n = len(nums)
        count = Counter(nums)
        if len(count) == k:
            return list(set(nums))
        freqs = defaultdict(list)
        for key in count:
            freqs[count[key]].append(key)
        frequencies = list(freqs.keys())
        index = random.randint(0, len(frequencies) - 1)
        value = frequencies[index] # frequency value
        left = []
        right = []
        for freq in frequencies:
            if freq < value:
                left.extend(freqs[freq])
            else:
                right.extend(freqs[freq])
        
        result = []
        if k <= len(right):
            array = []
            for number in right:
                array.extend([number] * count[number])
            result.extend(self.topKFrequent(array, k))
        else: # k > len(right)
            result.extend(right)
            array = []
            for number in left:
                array.extend([number] * count[number])
            result.extend(self.topKFrequent(array, k - len(right)))
        return result