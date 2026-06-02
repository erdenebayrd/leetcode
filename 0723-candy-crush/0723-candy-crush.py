import pprint

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
            we can iterate through every cells in 2 way
                1. horizonal way
                2. vertical way
            set cells whether needed to be deleted or not by 1, 0. 1 means need to be deleted, otherwise 0 in a different board named to_delete
            later on, update the to_delete array as an prefix sum from bottom to up
            the number on each cell in to_delete is saying this cell needed to be shifted down by how many rows
            by following that, update the cells, start again until there is no update appeared
            total time would be O(n ^ 4 / 3), space O(n ^ 2)
        """
        # time: O(n ^ 4)
        # space: O(n ^ 2)
        # method: simulation

        rows = len(board)
        cols = len(board[0])
        to_delete = [[0] * cols for _ in range(rows)]

        def crush(board, to_delete) -> bool: # any crush operation happen or not
            is_crush = False
            # horizontal
            for row in range(rows):
                for col in range(2, cols):
                    if board[row][col] != 0 and board[row][col] == board[row][col - 1] == board[row][col - 2]:
                        to_delete[row][col] = to_delete[row][col - 1] = to_delete[row][col - 2] = 1
                        is_crush = True
            
            # vertical
            for col in range(cols):
                for row in range(2, rows):
                    if board[row][col] != 0 and board[row][col] == board[row - 1][col] == board[row - 2][col]:
                        to_delete[row][col] = to_delete[row - 1][col] = to_delete[row - 2][col] = 1
                        is_crush = True
            
            # crush on board
            for row in range(rows):
                for col in range(cols):
                    if to_delete[row][col] == 0:
                        continue
                    board[row][col] = 0

            # update to_delete
            for row in range(rows - 2, -1, -1):
                for col in range(cols):
                    to_delete[row][col] += to_delete[row + 1][col]

            return is_crush
        
        def shift_down(board, to_delete) -> None: # updateing board by to_delete
            for row in range(rows - 2, -1, -1):
                for col in range(cols):
                    if to_delete[row + 1][col] == 0:
                        continue
                    destination_row = row + to_delete[row + 1][col]
                    board[destination_row][col] = board[row][col]
                    board[row][col] = 0
            for col in range(cols):
                if to_delete[0][col] == 0:
                    continue
                destination_row = to_delete[0][col] - 1
                board[destination_row][col] = 0

        while crush(board, to_delete):
            shift_down(board, to_delete)
            # pprint.pp(board)
            # print("-" * 100)
            to_delete = [[0] * cols for _ in range(rows)]
        
        return board