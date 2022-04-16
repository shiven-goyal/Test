#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 04:30:28 2022

@author: shivengoyal
"""

"""
Climbing Stairs
Easy

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        fibonnaci_list = [1,2]
        
        for i in range(3,n+1):
            fibonnaci_list.append(fibonnaci_list[-1] + fibonnaci_list[-2])
            print (fibonnaci_list)
            
        return fibonnaci_list[n-1]