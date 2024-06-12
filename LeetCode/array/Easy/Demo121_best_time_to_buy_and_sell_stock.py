class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # [7,6,4,3,1]
        # [7,1,5,3,6,4]
        # [2,4,1]
        # max_val = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         max_val = max(max_val, (prices[j] - prices[i]))
        # return max_val
        max_val = 0
        buy_index = 0
        for i in range(1, len(prices)):
            max_val = max(max_val, prices[i] - prices[buy_index])
            if prices[i] < prices[buy_index]:
                buy_index = i
        return max_val
