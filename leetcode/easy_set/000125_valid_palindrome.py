##########
#Question#
##########
'''
URL: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

'''


##########
#Solution#
##########

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=0:
            return True
        # print(s.lower())
        new_s = []
        palen=True
        for c in s:
            if c.isalnum():
                new_s.append(c.lower())
        j=len(new_s)-1
        for i in range(len(new_s)//2):
            if new_s[i]!=new_s[j-i]:
                palen=False
                break
        
        return palen
            
