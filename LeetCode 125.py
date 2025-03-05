class Solution:
    def isPalindrome(self, s: str) -> bool:
        pl = 0
        pr = len(s) - 1

        while pl < pr:
            if not s[pl].isalnum():
                pl += 1
                continue
            if not s[pr].isalnum():
                pr -= 1
                continue

            if s[pl].lower() != s[pr].lower():
                return False
            
            pl += 1
            pr -= 1

            
        return True