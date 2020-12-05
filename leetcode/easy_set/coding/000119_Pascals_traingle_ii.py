##########
#Question#
##########
'''
URL: https://leetcode.com/problems/pascals-triangle-ii/
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''


##########
#Solution#
##########

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
        result = []
        for i in range(rowIndex+1):
            tempResult=[]
            for j in range(0,i+1):
                if j in (0,i):
                    tempResult.append(1)
                else:
                    tempResult.append(result[j-1]+result[j])

            result=tempResult
        return result
                
        
        
