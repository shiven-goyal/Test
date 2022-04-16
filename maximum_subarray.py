#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 03:21:06 2022

@author: shivengoyal
"""

"""
Maximum Subarray
Easy

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        # SOLUTION 1 - BRUTE FORCE
        
        """
        sub_array = []
        max_sum = sum(nums)
        
        for i in range(0, len(nums) + 1):
            for j in range(i+1, len(nums) + 1):
                
                sub_array = nums[i:j]
                print (sub_array)
                addition = sum(sub_array)
                
                if(addition > max_sum):
                    max_sum = addition
        
                if(max_sum < nums[i]):
                    max_sum = nums[i]
                print(addition)
                    
        
        return max_sum
        """
        
        # SOLUTION 2 - DYNAMIC PROGRAMMING
        
        """ WRONG
        sum = nums[0]
        sum2 = nums[-1]
        List_Sum = []
        
        for i in nums[1:]:
            if (i+sum > sum):
                sum = i+sum
                List_Sum.append(sum)
            else:
                sum = i
                
        print ("array of sum is: ", List_Sum)
        if (max(List_Sum) > sum2):
            return max(List_Sum)
        else:
            return sum2
        """
        
        # SOLUTION 3 - DYNAMIC PROGRAMMING
        
        max_sum = nums[0]
        sum = nums[0]
        
        for i in nums[1:]:
            sum = max(i,sum+i)
            max_sum = max(max_sum,sum)
            
        return max_sum