class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = nums[0]
        profit = 0

        for i in range(1,len(prices)):
            curr_profit = price[i] - min_price
            if curr_profit > profit:
                profit = curr_profit
            min_price = min(min_price,prices[i])
        return profit
