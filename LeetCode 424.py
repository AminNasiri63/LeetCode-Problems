# 424. Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp, longest = 0, 0
        n = len(s)
        counts = [0] * 26

        for rp in range(n):
            counts[ord(s[rp]) - 65] += 1

            while (rp - lp + 1) - max(counts) > k:
                counts[ord(s[lp]) - 65] -= 1
                lp += 1
                print(rp, lp, counts)

            w = rp - lp + 1
            longest = max(longest, w)

        return longest
