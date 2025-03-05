class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ind = len(s)
        lenght = 0

        while ind > 0:
            ind -= 1
            if s[ind] != ' ':
                lenght += 1
            elif lenght != 0:
                break
        return lenght