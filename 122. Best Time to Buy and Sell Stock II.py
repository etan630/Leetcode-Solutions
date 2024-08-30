#medium
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        length = len(prices)

        if length == 0:
            return 0

        maxp = 0

        # buy if current is cheaper next day so you can sell
        for i in range (1, length):
            if prices[i] > prices[i - 1]:
                maxp += prices[i] - prices[i - 1]
        

        return maxp
