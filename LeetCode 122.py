class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyPrice = prices[0]
        profit = 0

        for p in prices[1:]:
            if p < buyPrice:
                buyPrice = p
            
            if p - buyPrice > 0:
                profit += p - buyPrice
                buyPrice = p
        
        return profit
        