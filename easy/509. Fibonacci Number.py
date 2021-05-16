'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

SOL: iterative approach
'''
class Solution:
    def fib(self, n: int) -> int:
        fibarr = [0 for i in range(31)]
        fibarr[1] = 1
        if n < 2:
            return fibarr[n]
        for i in range(n-1):
            fibarr[i+2] = fibarr[i+1] + fibarr[i]
        return fibarr[n]