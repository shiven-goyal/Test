#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 23:54:43 2022

@author: shivengoyal
"""
"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        str_return = []
        
        for i in strs:
            list = str(sorted(i)) # sorted i gives list which cannot be used 
            # as key in dict.
            
            if list in dict:
                dict[list].append(i)
                
            else:
                dict[list] = [i]  # make sure to assing value in [], since we are appending in list.
       # print("Dictionary IS", dict)
            
        for key, value in dict.items():
                str_return.append(value)
                
        return str_return
        print (str_return)
        
            
        