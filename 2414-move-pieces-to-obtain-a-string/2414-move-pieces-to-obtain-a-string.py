class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_pieces = [(char, i) for i, char in enumerate(start) if char != '_']
        target_pieces = [(char, i) for i, char in enumerate(target) if char != '_']

        if len(start_pieces) != len(target_pieces):
            return False
        for (s_char, s_idx), (t_char, t_idx) in zip(start_pieces, target_pieces):
            if s_char != t_char:
                return False
            if s_char == 'L' and s_idx < t_idx:  # 'L' cannot move right
                return False
            if s_char == 'R' and s_idx > t_idx:  # 'R' cannot move left
                return False

        return True