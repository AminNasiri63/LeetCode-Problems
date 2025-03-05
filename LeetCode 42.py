class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        # l_wall = r_wall = 0

        for i in range(1, n):
            j = -i - 1
            # maxleft[i] = l_wall
            # maxright[j] = r_wall
            # l_wall = max(l_wall , height[i])
            # r_wall = max(r_wall , height[j])

            maxleft[i] = max(height[i-1], maxleft[i-1])
            maxright[j] = max(height[j+1], maxright[j+1])

        trapped = 0
        for i in range(n):
            water = min(maxleft[i], maxright[i])
            trapped += max(0, water - height[i])
            # if height[i] <= water:
            #     trapped += water - height[i]
        
        return trapped