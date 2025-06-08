class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        # Start generating numbers from 1 to 9
        for start in range(1, 10):
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
        return lexicographical_numbers

    def _generate_lexical_numbers(
        self, current_number: int, limit: int, result: List[int]
    ):
        # If the current number exceeds the limit, stop recursion
        if current_number > limit:
            return
        # Add the current number to the result
        result.append(current_number)

        # Try to append digits from 0 to 9 to the current number
        for next_digit in range(10):
            next_number = current_number * 10 + next_digit
            # If the next number is within the limit, continue recursion
            if next_number <= limit:
                self._generate_lexical_numbers(next_number, limit, result)
            else:
                break  # No need to continue if next_number exceeds limit