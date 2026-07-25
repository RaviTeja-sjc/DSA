class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            result = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(s[i - 1])
                    count = 1

            result.append(str(count))
            result.append(s[-1])

            s = "".join(result)

        return s