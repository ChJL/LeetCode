# Tag: Dynamic Programming
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

SOL: (HuaHua: https://www.youtube.com/watch?v=oL6mRyTn56M)
         
            ___rest    ___rest
            |  |       |   |
            |  v       |   v
[sold] --> [rest] ---> [hold]
  ^                      | 
  |______________________|
           sell

hold[i] = max( hold[i-1],  rest[i-1]-prices[i])
sold[i] = hold[i-1] + prices[i]
rest[i] = max( rest[i-1], sold[i-1])
init: hold[0] = -inf, sold[0] = 0, rest[0] = 0
           
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -10000000
        sold = 0
        rest = 0
        
        for i in range(len(prices)):
            hold_new = max(hold, rest-prices[i])
            sold_new = hold + prices[i]
            rest_new = max(rest, sold)
            
            hold = hold_new
            sold = sold_new
            rest = rest_new
        
        return sold if sold>rest else rest