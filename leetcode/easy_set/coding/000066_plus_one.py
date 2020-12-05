##########
#Question#
##########
'''
URL: https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9

'''


##########
#Solution#
##########
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        if digits[-1] < 9:
            digits[-1]+=1
        else:
            digits[-1]=0
            carry=1
            for i in range(len(digits)-2,-1,-1):
                num = digits[i]+carry
                if num > 9:
                    digits[i] = 0
                    carry=1
                else:
                    digits[i] = num
                    carry=0
                    break
                
            if carry == 1:
                digits[0]=carry
                digits.append(0)
           
        return digits
        

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        total=0
        for i in range(0,len(digits)):
            total += digits[i]*(10**i)
        total = total+1
        return [int(d) for d in str(total)]
