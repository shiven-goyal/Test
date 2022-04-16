#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:19:38 2022

@author: shivengoyal
"""

"""Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'. """


# SOLUTION

# Solution 1 : Hash Table : Time Complexity ~= 32 ms

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','[':']','{':'}'}
        stack = deque()
        str_final = ''
        
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    stack_key = stack.pop()  # stack_key is value in stack
                    if d[stack_key] == i:
                        str_final = str_final + stack_key + i
        
        if (len(str_final) == len(s)):
            return True
        

# Solution 2 : Using Sets : Time Complexity ~= 28 ms
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in {'{','[','('}:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False
        if stack:
            return False
        return True
        