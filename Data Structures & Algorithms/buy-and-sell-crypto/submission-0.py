class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_value = float('inf')
        sell_value = 1
        # buy_value_index = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy_value:
                buy_value = prices[i]
                # buy_value_index = i
            else:
                profit_today = prices[i] - buy_value
                profit = max(profit, profit_today)
        
        # for i in range(len(prices)):
        #     if sell_value > buy_value and sell_value > prices[i] and i>buy_value_index:
        #         sell_value = prices[i]
        # profit = sell_value - buy_value

        return profit