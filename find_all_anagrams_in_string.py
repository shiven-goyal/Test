#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:25:00 2022

@author: shivengoyal
"""

"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        """
        list_indices = []
        ana_str = ''
        
        for i in range(0, len(s) + 1):
            for j in range(i+1, len(s) + 1):
                ana_str = s[i:j]
                print(ana_str, p)
                
                if(len(ana_str) == len(set(p)) and set(ana_str) == set(p)):
                    list_indices.append(i)
                    
        return list_indices
        """
        
        # SOLUTION 1 - HASH MAP - Time Complexity - O(n), Space Complexity - 
        """
        s_map = [0]*26
        p_map = [0]*26
        
        if len(p) > len(s):
            return []
        
        for i in p:
            p_map[ord(i) - 97] += 1
            
        output = []
        
        for i in range (0,len(s)):
            s_map[ord(s[i]) - 97]+= 1
            
            if i >= len(p):
                s_map[ (ord(s[i - len(p)])) - 97]-=1
                
            if (s_map == p_map):
                output.append(i - len(p) + 1)
            
        return output
        """
        
        