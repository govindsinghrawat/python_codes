##########
#Question#
##########
'''
URL: https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''


##########
#Solution#
##########

class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = []
        for i in range(numRows):
            row = []
            for j in range(0, i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1]+result[i-1][j])
            result.append(row)
        
        return result
                

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = []
        for i in range(numRows):
            #append[]
            result.append([])
            
            
            for j in range (i+1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
                    
        return result
