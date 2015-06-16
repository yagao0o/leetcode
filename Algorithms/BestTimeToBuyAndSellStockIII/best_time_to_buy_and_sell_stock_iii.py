# Author  :  Yagao0o
# Date    :  2015-03-03
# Source  :  https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        return self.max_profit(2, prices)

    def max_profit(self, k, prices):
        # it's a DP problem
        # f(k, i) the profit of the ith day by k transactions:
        # f(k, i) = max( f(k, i - 1),                               max_profit of (i-1) day
        #                max(f(k - 1,j) + prices[i] - prices[j])    i = 1 to j max_profit k - 1 transactions in day j
        #              )                                               and buy at day j sell at  day i
        # f(0, i) = 0   f(k, 0) = 0
        # for a special i:
        #     max(f(k-1, j) + prices[i] - prices[j]) = max(f(k-1, j) - prices[j]) + prices[i]   //   part2 + prices[i]
        #
        # another DP sub-problem:
        #     part2(k, i) = max( part2(k, i - 1), f(k - 1, i) - prices[i] )
        #     part2(k, 0) = -prices[0]
        # so:
        # f(k ,i) = max( f(k, i - 1), max_part2( k - 1, i - 1) + prices[i] )
        f = [0] * len(prices)
        for transaction_times in range(1, k + 1):
            part2_max = -prices[0]
            for i in range(1, len(f)):
                max_profit_with_day_i = part2_max + prices[i]
                part2_max = part2_max if part2_max >= f[i] - prices[i] else f[i] - prices[i]
                f[i] = f[i - 1] if f[i - 1] >= max_profit_with_day_i else max_profit_with_day_i
        return f[len(f) - 1]

a = Solution()
print a.maxProfit([0,5,4,7,5,6])