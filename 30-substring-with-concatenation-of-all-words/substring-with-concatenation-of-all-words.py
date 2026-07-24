from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        target = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            count = 0
            window = defaultdict(int)

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    window[word] += 1
                    count += 1

                    while window[word] > target[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        res.append(left)
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return res