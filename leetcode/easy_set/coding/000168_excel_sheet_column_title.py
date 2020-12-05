##########
#Question#
##########
'''
URL: https://leetcode.com/problems/excel-sheet-column-title/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''


##########
#Solution#
##########

class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <1:
            return ""
        
        result=""
        
        while n > 0:
            result=result+str(chr(65 +(n-1)%26))
            n = (n-1)//26
            
        return result[::-1]
        
        
