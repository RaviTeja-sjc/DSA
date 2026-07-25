class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Fill the sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":

                        box = (r // 3) * 3 + (c // 3)

                        for num in "123456789":

                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[box]):

                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box].add(num)

                                if solve():
                                    return True

                                board[r][c] = "."
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box].remove(num)

                        return False

            return True

        solve()

          