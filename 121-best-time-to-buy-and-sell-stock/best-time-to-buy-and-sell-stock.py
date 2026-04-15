class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')  # very large number
        max_profit = 0
        
        for price in prices:
            # update minimum price
            if price < min_price:
                min_price = price
            
            # calculate profit
            profit = price - min_price
            
            # update max profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit