from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6

        freq = Counter(s)

        mid = ""
        half = {}

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ch] = freq[ch] // 2

        total_len = sum(half.values())

        def ways(cnt):
            rem = sum(cnt.values())
            ans = 1

            for ch in sorted(cnt):
                f = cnt[ch]
                if f:
                    ans *= comb(rem, f)
                    if ans > LIMIT:
                        return LIMIT
                    rem -= f
            return ans

        if ways(half) < k:
            return ""

        first = []

        for _ in range(total_len):

            for ch in sorted(half):

                if half[ch] == 0:
                    continue

                half[ch] -= 1

                cnt = ways(half)

                if cnt >= k:
                    first.append(ch)
                    break

                k -= cnt
                half[ch] += 1

        left = "".join(first)
        return left + mid + left[::-1]