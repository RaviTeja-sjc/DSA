class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []

        def backtrack(i, target):

            if target == 0:
                result.append(path[:])
                return

            if i == len(candidates) or target < 0:
                return

            # Take current number
            path.append(candidates[i])
            backtrack(i, target - candidates[i])
            path.pop()

            # Skip current number
            backtrack(i + 1, target)

        backtrack(0, target)

        return result