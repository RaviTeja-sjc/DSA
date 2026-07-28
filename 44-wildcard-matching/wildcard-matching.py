class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        prev = [False] * (n + 1)
        curr = [False] * (n + 1)

        prev[n] = True

        # Empty string vs remaining pattern
        for j in range(n - 1, -1, -1):
            prev[j] = p[j] == '*' and prev[j + 1]

        for i in range(m - 1, -1, -1):
            curr[n] = False

            for j in range(n - 1, -1, -1):

                if p[j] == '*':
                    curr[j] = curr[j + 1] or prev[j]

                elif p[j] == '?' or s[i] == p[j]:
                    curr[j] = prev[j + 1]

                else:
                    curr[j] = False

            prev, curr = curr, [False] * (n + 1)

        return prev[0]