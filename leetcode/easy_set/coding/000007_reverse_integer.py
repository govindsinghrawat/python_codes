##########
#Question#
##########
'''
URL: https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-2**31 <= x <= 2**31 - 1
'''


##########
#Solution#
##########
class Solution:
    def reverse(self, x: int) -> int:
        is_negative=False
        if x<0:
            x*=-1
            is_negative=True
        
        num = str(x)[::-1]
        
        if is_negative:
            return 0 if int(num)*-1 < -2**31 else int(num)*-1
        else:
            return 0 if int(num) > (2**31 -1) else int(num)
        
