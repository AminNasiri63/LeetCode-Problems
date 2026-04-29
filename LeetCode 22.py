# 22. Generate Parentheses

from typing import List


#  C(n) = (2n)! / ((n + 1)! * n!), Time: O(C(n) * n) - Space: O(C(n) * n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol, res = [], []

        def backtrack(open, close):
            if len(sol) == 2*n:
                res.append("".join(sol))
                return

            if open < n:
                sol.append('(')
                backtrack(open+1, close)
                sol.pop()

            if close < open:
                sol.append(')')
                backtrack(open, close+1)
                sol.pop()

        backtrack(0, 0)

        return res





