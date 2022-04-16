#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:15:54 2022

@author: shivengoyal
"""

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # - SOLUTION 1 - BRUTE FORCE
        """
        list_2 = []
        
        for i in range(0, len(nums)):
            if (nums[i] in list_2):
                list_2.remove(nums[i])
            else:
                list_2.append(nums[i])
        
        print (list_2)
        return list_2[0]
        """
        
        # - SOLUTION 2 - DICTIONARY
        """
        dict = {}
        
        for i in range(0, len(nums)):
            if (nums[i] in dict):
                dict[nums[i]] = nums[i]
            else:
                dict[nums[i]] = 40000
        
        for key,value in dict.items():
            if value == 40000:
                print (key)
                return key
        """
        
        # - SOLIUTION 3 - DEFAULT DICTIONARY HONEY'S SOLIUTION
        
        dict = defaultdict(lambda:0)
        for i in nums:
            dict[i] = dict[i] + 1
        
        for key,value in dict.items():
            if(value == 1):
                return key
        
        
        
            
        
        
        
