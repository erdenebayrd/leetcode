class Solution(object):
    def numRabbits(self, answers):
        count = collections.Counter(answers)
        return sum(-v % (k+1) + v for k, v in count.items())