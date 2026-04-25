# 77. Combinations


from typing import List


# Time: O(n choose k) - Space: O(n)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, res = [], []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return

            should_pick = k - len(sol)

            if x > should_pick:  # x is left num
                backtrack(x-1)

            sol.append(x)
            backtrack(x-1)
            sol.pop()

        backtrack(n)

        return res

# Method 2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, res = [], []

        def backtrack(s):
            if len(sol) == k:
                res.append(sol[:])
                return

            for num in range(s, n+1):
                sol.append(num)
                backtrack(num+1)
                sol.pop()

        backtrack(1)

        return res



