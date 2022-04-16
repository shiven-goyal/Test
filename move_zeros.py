#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 00:22:45 2022

@author: shivengoyal
"""

"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # SOLUTION 1- BRUTE FORCE
        
        """
        non_zero = []
        zero = []
        list_final = []
        
        for i in range(0,len(nums)):
            if(nums[i] == 0):
                zero.append(nums[i])
            else:
                non_zero.append(nums[i])
                
        list_final = non_zero + zero
        
        for i in range(0, len(nums)):
            nums[i] = list_final[i]
        """
        
        # SOLUTION 2 - SWAP 
        
        i = 0
        
        for j in range(0, len(nums)):
            
            if (nums[j] != 0):
                nums[i] = nums[j]
                i = i +1
            
            
        for x in range(i, len(nums)):
            nums[x] = 0
            

        