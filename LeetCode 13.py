class Solution:
    def romanToInt(self, s: str) -> int:

        RomanDic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,
        'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        res = 0
        pl = 0
        
        while pl < len(s):
            if pl < len(s) - 1 and RomanDic[s[pl]] < RomanDic[s[pl+1]]:
                res += RomanDic[s[pl+1]] - RomanDic[s[pl]]
                pl += 2
                continue
            res += RomanDic[s[pl]]
            pl += 1
        
        return res

        