#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 02:23:37 2022

@author: shivengoyal
"""

"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # SOLUTION 1 - DICTIONARY HASH TABLE - O(n)
        
        """
        dict = {}
        list = []
        
        for i in range(0, len(nums)):
            dict[i+1] = 0
        
            
        for i in range(0, len(nums)):
            if nums[i] in dict:
                dict[nums[i]] = dict[nums[i]] + 1
                
        for key,value in dict.items():
            if(value == 0):
                list.append(key)
                
        return list
        """
        
        # SOLUTION 2 - USING SET - O(n), No extra space
        
        print(set(range(1, len(nums)+1)))
        return list((set(range(1, len(nums) + 1)) - set(nums)))
        
            
            
        