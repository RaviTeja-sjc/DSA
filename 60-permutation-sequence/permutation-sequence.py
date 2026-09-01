class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        numbers = list(range(1, n + 1))

        # Convert k to 0-based indexing
        k -= 1

        result = []

        # Factorials
        factorial = 1

        for i in range(1, n):
            factorial *= i

        for remaining in range(n, 0, -1):

            # Find which block k belongs to
            index = k // factorial

            # Select that number
            result.append(str(numbers.pop(index)))

            # Move k inside the selected block
            k %= factorial

            # Calculate factorial for next position
            if remaining > 1:
                factorial //= (remaining - 1)

        return ''.join(result)