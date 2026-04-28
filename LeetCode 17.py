# 17. Letter Combinations of a Phone Number


from typing import List


# Time: O(n * 4^n) - Space: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        sol, res = [], []
        n = len(digits)
        digits_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                      '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(i):
            if i == n:
                res.append("".join(sol))
                return

            for letter in digits_map[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()

        backtrack(0)

        return res


