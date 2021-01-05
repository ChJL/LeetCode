# 524. Longest Word in Dictionary through Deleting
'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed 
by deleting some characters of the given string. If there are more than one possible results, 
return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"

'''

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # -len(x) 讓長的字放前面, x 照字典序
        # sortword = sorted(d, key = (lambda x:(-len(x),x)) )
        MAX_len = 0
        res =[]
        ans1 = ""
        for word in d:
            i = 0
            #flag = 0
            
            for j in s:
                if (j == word[i]):
                    i += 1
                if (i == len(word)):    
                    if( i> MAX_len):
                        res.clear()
                        res.append(word)
                        MAX_len = i
                    elif(i == MAX_len):
                        
                        res.append(word)
                        
                    break
                            
        if (len(res)>0 ):
            ans = sorted(res, key = (lambda x:x))
            return ans[0]
            
            
        return ""