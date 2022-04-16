#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:56:36 2022

@author: shivengoyal
"""


"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # SOLUTION 1 - DICTIONARY HASH TABLE- O(n) time and O(1) space.
        
        """
        dict = defaultdict(lambda:0)
        
        for i in range(0, len(nums)):
            dict[nums[i]] = dict[nums[i]] + 1
            
        for key,value in dict.items():
            if (value >  (len(nums)/2)):
                return key
                
        """