
# 509. Fibonacci Number

# recurcive method
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)

# top-down method
class Solution:
    def fib(self, n: int) -> int:
        sol = {0:0, 1:1}

        def fun(x):
            if x in sol:
                return sol[x]
            else:
                sol[x] = fun(x-1) + fun(x-2)
                return sol[x]

        return fun(n)

# bottom-up method
class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        sol = [0] * (n+1)
        sol[0], sol[1] = 0, 1

        for i in range(2, n+1):
            sol[i] = sol[i-1] + sol[i-2]

        return sol[n]

# constant space method
class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        prev, cur = 0, 1

        for _ in range(2, n+1):
            prev, cur = cur, cur+prev

        return cur