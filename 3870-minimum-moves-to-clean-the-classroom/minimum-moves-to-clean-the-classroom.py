from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter cell
        start_r = start_c = -1
        litter_id = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # All litter collected mask
        target = (1 << litter_count) - 1

        # BFS:
        # (row, col, collected_mask, remaining_energy)
        queue = deque()
        queue.append((start_r, start_c, 0, energy, 0))

        # visited states
        visited = set()
        visited.add((start_r, start_c, 0, energy))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, mask, curr_energy, moves = queue.popleft()

            # We collected everything
            if mask == target:
                return moves

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Need energy to make this move
                if curr_energy == 0:
                    continue

                # Spend one energy
                new_energy = curr_energy - 1

                # Collect litter
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    litter_index = litter_id[(nr, nc)]
                    new_mask |= (1 << litter_index)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # If energy is 0 and we're NOT on R,
                # we cannot continue from here.
                state = (nr, nc, new_mask, new_energy)

                if state in visited:
                    continue

                visited.add(state)

                queue.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1       