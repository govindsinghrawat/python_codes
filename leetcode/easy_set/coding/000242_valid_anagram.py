##########
#Question#
##########
'''
URL: https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''


##########
#Solution#
##########
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         sn = len(s)
#         tn = len(t)
        
#         if sn != tn:
#             return False
        
#         anagram_dict = {}
        
#         for c in s:
#             if c in anagram_dict.keys():
#                 anagram_dict[c]+=1
#             else:
#                 anagram_dict[c]=1
        
#         for c in t:
#             if c in anagram_dict.keys():
#                 anagram_dict[c]-=1
#             else:
#                 return False
        
#         for _, value in anagram_dict.items():
#             if value !=0:
#                 return False
        
#         return True
          return collections.Counter(s) == collections.Counter(t)
