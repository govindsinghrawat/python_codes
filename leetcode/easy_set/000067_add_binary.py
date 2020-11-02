##########
#Question#
##########
'''
URL: https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

'''


##########
#Solution#
##########
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        
        carry = 0
        a=a.zfill(max_len)
        b=b.zfill(max_len)
        result=''
        sum_tot=0
        
        for i in range(max_len-1,-1,-1):
            sum_tot = carry+int(a[i]) + int(b[i])
            
            if sum_tot ==3:
                
                result='1'+ result
                carry=1
            elif sum_tot ==2:
                result='0'+ result
                carry=1
            
            elif sum_tot == 1:
                result = '1' + result
                carry=0
            else:
                result = '0' + result
                carry=0
        
        return result if carry==0 else "1"+result

class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        
        a = int(a)
        b = int(b)
        
        if a == 0 and b == 0:
            return "0"
        
        
        s, c = "", 0
        
        while a!=0 or b!=0:
            
            u1 = a%10
            u2 = b%10
            
            a = a//10
            b = b//10
            
            
            tsum = u1+u2+c
            
            if tsum == 3:
                c = 1
                tsum = 1
                
            elif tsum == 2:
                c = 1
                tsum = 0
                
            elif tsum == 1:
                tsum = 1
                c = 0
                
            elif tsum == 0:
                tsum = 0
                c = 0
                
            
            s = str(tsum)+s
            
        if c == 1:
            s = '1'+s
            
        
        return str(s)
