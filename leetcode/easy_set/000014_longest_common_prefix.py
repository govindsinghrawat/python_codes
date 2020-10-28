##########
#Question#
##########
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''


##########
#Solution#
##########
        class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_prefix = ""
        
        if len(strs) == 0:
            return result_prefix
        
        if len(strs) == 1:
            return strs[0]
        
        first_str=strs[0]
        for i in range(1,len(strs)):
            result_prefix= self.compare(first_str, strs[i])
            
            
            if result_prefix == "":
                break
                
            first_str=result_prefix
        
        return result_prefix
        
    def compare(self, str1:str, str2: str) -> str:
        return_str = ""
        
        min_len = min(len(str1), len(str2))
        if min_len < 1:
            return return_str
        
        
        
        for i in range(0, min_len):
            if str1[i] != str2[i]:
                break
            return_str = return_str+str1[i]
            print(return_str)
        
        return return_str
