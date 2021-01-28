# Tag: Math
'''
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).


Example:
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.


SOL:
  f(i)          = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... +  (k-1) * A[k-1] + k * A[k]
  f(i+1)        = 1 * A[0] + 2 * A[1] + 3 * A[2] + ...  +     k  * A[k-1] + 0 * A[k] 
=>f(i+1) - f(i) =     A[0]   +   A[1]   +   A[2] + ...  +       A[k-1]    - k * A[k] 
   = (A[0]   +   A[1]   +   A[2] + ...  +       A[k-1] +  A[k])  - (k+1) * A[k]
   = sum(Array) - A[k] * array.length
=> f(i+1) = f(i) + sum(Array) -  last element * array.length
'''


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        i = 0
        sumA = 0
        f0 = 0
        
        while i < len(A):
            sumA += A[i]
            f0 += i*A[i]
            i += 1
        
        ans = f0
        f = f0
        n = len(A)
        for i in range(len(A)-1):
            f = f + sumA - n*A[n-i-1]
            ans = max(f, ans)
        
        return ans