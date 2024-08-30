class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0

        minp = [0] * length
        maxp = [0] * length


        # set init
        minp[0] = prices[0]
        maxp[0] = 0

        # start day 2
        for i in range (1, length):
            minp[i] = min(minp[i - 1], prices[i])

            #prev max vs curr profit
            maxp[i] = max(maxp[i - 1], prices[i] - minp[i])
        
        return maxp[length - 1]
