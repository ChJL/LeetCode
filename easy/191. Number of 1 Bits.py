#Tag:  Bit manipulation
'''
Write a function that takes an unsigned integer and returns 
the number of '1' bits it has (also known as the Hamming weight).

SOL: 
method 1: if n mod2 == 1 -> count +1 

==========
method 2: 
Using bit operation to cancel a 1 in each round

Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. 
n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
: fast than method 1

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!= 0:
            n = n & (n-1)
            count += 1    
        return count

'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!= 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count