class Solution:
    def stoneGameVI(self, alice_values: List[int], bob_values: List[int]) -> int:
        # time: O(N log N)
        # space: O(N)
        # method: sorting + greedy
        values = sorted(zip(alice_values, bob_values), key=sum, reverse=True)
        is_alice_turn = True
        alice = bob = 0
        for alice_value, bob_value in values:
            if is_alice_turn:
                alice += alice_value
            else:
                bob += bob_value
            is_alice_turn = not is_alice_turn
        if alice > bob:
            return 1
        elif bob > alice:
            return -1
        return 0