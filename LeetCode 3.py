# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        longest = 0
        chr_set = set()
        n = len(s)

        for rp in range(n):

            while s[rp] in chr_set:
                chr_set.remove(s[lp])
                lp += 1

            chr_set.add(s[rp])
            w = rp - lp + 1
            longest = max(longest, w)

        return longest
