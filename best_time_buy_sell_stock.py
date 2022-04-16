#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:25:08 2022

@author: shivengoyal
"""

"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # SOLUTION 1 - BRUTE FORCE
        """
        profit = 0
        max_profit = 0
        
        for i in range(0, len(prices) - 1):
            for j in range(i+1, len(prices)):
                
                if((prices[j] - prices[i]) > 0):
                    profit = prices[j] - prices[i]
                    if (profit > max_profit):
                        max_profit = profit
            
                        
        print(max_profit)
        return max_profit
        """
        
        # SOLUTION 2 - DYNAMIC PROGRAMMING
        
        profit = 0
        min_price = prices[0]
        
        for i in prices[1:]:
            min_price = min(min_price, i)
            profit = max(profit, i-min_price)
            
        print(profit)
        return profit
        
        
                    
        
        