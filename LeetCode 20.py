# 20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {")": "(", "}": "{", "]": "["}
        chrs = []

        for c in s:
            if c not in hashmap:
                chrs.append(c)

            else:
                if not chrs:
                    return False
                else:
                    last = chrs.pop()
                    if last != hashmap[c]:
                        return False

        return not chrs



