class Solution:
    def maxArea(self, height: List[int]) -> int:

        lp = 0
        rp = len(height) - 1
        maxW = 0

        while lp < rp:
            w = rp - lp
            h = min(height[lp], height[rp])
            area = w*h

            maxW = max(area, maxW)

            if height[lp] <= height[rp]:
                lp += 1
            else:
                rp -= 1
        
        return maxW
