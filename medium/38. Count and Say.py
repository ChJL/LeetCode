# Tag: string
'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

Hint:
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

SOL: simple string operation
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        start = "1"
        
        for i in range(n-1):
            j = 0
            tmp = ""
            cur = ""
            count = 0
            while j < len(start):
                if start[j] != cur:
                    if cur and count:
                        tmp = tmp + str(count) + cur
                        count = 0
                    cur = start[j]
                    count +=1
                else:
                    count +=1
                j+=1
            
            # the last case, but is not include in while loop
            start = tmp + str(count) + cur
        
        return start
                    