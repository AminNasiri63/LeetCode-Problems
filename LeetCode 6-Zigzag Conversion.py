class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows >= len(s) or numRows == 1:
            return s

        res = ''

        for i in range(numRows):
            res += s[i]
            skipr = 2 * (numRows-i-1)
            skipl = 2 * i
            j = i
            while True:

                if skipr > 0:
                    j += skipr
                    if j > len(s) - 1:
                        break
                    res += s[j]
                
                if skipl > 0:
                    j += skipl
                    if j > len(s) - 1:
                        break
                    res += s[j]
        return res