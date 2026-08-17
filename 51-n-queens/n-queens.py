class Solution:
    def solveNQueens(self, n: int):
        result = []

        # Create empty board
        board = [["."] * n for _ in range(n)]

        # Sets to keep track of attacked columns and diagonals
        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):

            # If all rows are completed,
            # we found a valid solution
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                result.append(solution)
                return

            # Try placing queen in every column
            for col in range(n):

                # Same column
                if col in cols:
                    continue

                # Same diagonal
                if row - col in diag1:
                    continue

                # Same diagonal
                if row + col in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack: remove queen
                board[row][col] = "."

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Start from row 0
        backtrack(0)

        return result