# Tag: Dynamic Programming

'''
You are given an array prices for which prices[i] is the price of a given stock on the ith day.

You are only permitted to complete at most one transaction. 
In other words, you can buy one and sell one share of the stock. You cannot sell a stock before you buy one.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
The answer is not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

SOL: keep tracking the min_value, and update the expected maximum revenue
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        exp_rev = 0
        for i in range(1,len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            elif prices[i]-min_val > exp_rev:
                exp_rev = prices[i]-min_val
                    
        return exp_rev